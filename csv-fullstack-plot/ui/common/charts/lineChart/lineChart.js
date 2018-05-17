charts.directive('lineChart', ['$window', '$timeout', function($window, $timeout) {

    function renderChart(element, attrs, config) {
        // cleanup tooltips if any exist in the DOM
        d3.selectAll(".d3-tip lineChart").remove();

        var data = config.data;
        if (data !== undefined){
            data.forEach(function (line, i) {
                line.values.forEach(function (circle) {
                    circle.index = i;
                });
            });
        }


        // default attributes, overridden by configuration from controller
        var defaults = {
            // x axis
            labelX: "Period",
            scaleTypeX: "ordinal", // supported: ordinal, linear
            formatX: "d",
            scaleMaxX: null,
            scaleMinX: null,
            guidelinesX: true,
            labelRotationX: 0,
            tickFrequencyX: 1, // ie. every 1, every other, every 3rd
            tickSizeX: 8,
            // y axis
            labelY: "Value",
            formatY: "s",
            formatTooltipValue: ".2s", // if tooltip enabled, this defines formatting of numerical value
            scaleMaxY: null,
            scaleMinY: null,
            guidelinesY: true,
            labelRotationY: 0,
            tickFrequencyY: 1,
            tickSizeY: 8,
            legend: "right",
            tickCountY: 4, // rounds to create intervals of 2, 5, or 10
            // other settings
            circleRadius: 0,
            hoverLine: true,
            hoverSnap: true,
            hoverOut: true,
            tension: 1, // curved (0) to straight line (1)
            tooltip: false,
            margin: {top: 20, right: 60, bottom: 80, left: 60},
            events: {},
            styles: {
                classes: ["dashed", ""]
            },
            messages: {
                noData: "No Data Available"
            }
        };

        // copy over config overwriting the default settings
        for (var prop in config) {
            if (prop === 'styles') {
                for (var styleProp in config.styles) {
                    defaults.styles[styleProp] = config.styles[styleProp];
                }
            }
            defaults[prop] = config[prop];
        }

        var colorScale = defaults.styles.colors ? d3.scale.ordinal().range(defaults.styles.colors) : d3.scale.category20();

        var clientWidth = element[0].clientWidth;
        var clientHeight = element[0].clientHeight;

        var width = clientWidth - defaults.margin.left - defaults.margin.right;
        var height = clientHeight - defaults.margin.top - defaults.margin.bottom;

        // define base SVG element
        var svg = d3.select(element[0]).select("svg")
            .attr("width", width + defaults.margin.left + defaults.margin.right)
            .attr("height", height + defaults.margin.top + defaults.margin.bottom);

        var svgGroup = svg.select("g")
            .attr("transform", "translate(" + defaults.margin.left + "," + defaults.margin.top + ")");

        // define scales & axes
        if (defaults.scaleTypeX === "ordinal") {
            var xScale = d3.scale.ordinal()
                .rangeRoundBands([0, width], 1);
        }

        else {
            var xScale = d3.scale.linear()
                .range([0, width]);
        }

        var yScale = d3.scale.linear()
            .range([height, 0]);

        // set scales based on domain and range of data
        var valueArrays = _.reduce(data, function (result, arr) {
            return result.concat(arr.values);
        }, []);

        var periods = _.uniq(_.map(valueArrays, function (obj) {
            return obj.key;
        }, []));

        var values = _.uniq(_.map(valueArrays, function (obj) {
            return obj.values;
        }, []));

        if (defaults.scaleTypeX === "ordinal") {
            xScale.domain(periods);
        }

        else {
            var periodMin = defaults.scaleMinX || d3.max([0, d3.min(periods) - (d3.max(periods) / 20)]);
            var periodMax = defaults.scaleMaxX || d3.max(periods) + (d3.max(periods) / 20);
            xScale.domain([periodMin, periodMax]);
        }

        var boundryAdj = 0.1;
        var valueMin = d3.min(values) - Math.abs(d3.max(values) * boundryAdj);
        var valueMax = d3.max(values) + Math.abs(d3.max(values) * boundryAdj);

        if (defaults.scaleMaxY !== null) { valueMax = defaults.scaleMaxY; };
        if (defaults.scaleMinY !== null) { valueMin = defaults.scaleMinY; };

        yScale.domain([valueMin, valueMax]);

        // edge case where all y values are 0
        if (valueMin == 0 && valueMax == 0) {
            yScale.domain([valueMin - .05, valueMax + .05])
        }

        // set axes and gridlines if enabled
        if (defaults.scaleTypeX === "ordinal") {
            var xAxis = d3.svg.axis()
                .scale(xScale)
                .tickSize(defaults.tickSizeX, 0)
                .tickFormat(function(d) {return d; })
                .orient("bottom");

            var xGrid = d3.svg.axis()
                .scale(xScale)
                .tickSize(-height, 0)
                .tickFormat(function(d) {return d; })
                .orient("bottom");
        }
        else {
             var xAxis = d3.svg.axis()
            .scale(xScale)
            .tickSize(defaults.tickSizeX, 0)
            .tickFormat(function(d) { return d3.format(defaults.formatX)(d).replace('G', 'B'); })
            .orient("bottom");
        }

        var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left")
            .tickSize(defaults.tickSizeY, 0)
            .ticks(defaults.tickCountY)
            .tickFormat(function(d) { return d3.format(defaults.formatY)(d).replace('G', 'B'); });

        var yGrid = d3.svg.axis()
            .scale(yScale)
            .orient("left")
            .tickSize(-width)
            .ticks(defaults.tickCountY);

        // define line
        var line = d3.svg.line()
            .x(function (d) {
                return xScale(d.key);
            })
            .y(function (d) {
                return yScale(d.values);
            })
            .interpolate("cardinal")
            .tension(defaults.tension);

        // if no data, display message
        if (valueArrays == false) {
            svgGroup.attr("display", "none");
            svg.selectAll("text.no-data").remove();
            svg.append("text")
            .attr("class", "no-data")
            .attr("x", clientWidth / 2)
            .attr("y", clientHeight / 2)
            .attr("text-anchor", "middle")
            .text(function(d) { return defaults.messages.noData; })
        }
        
        else {
            // unhide chart group and remove no data message
            svg.selectAll("text.no-data").remove();
            svgGroup.attr("display", "inline");
            
            // draw axes & axis labels
            var xAxisEl = svgGroup.select("g.x.axis")
                .attr("transform", "translate(0," + height + ")")
                .transition()
            
            xAxisEl.call(xAxis);
            if (defaults.guidelinesX) { xAxisEl.call(xGrid); }

            // enable rotation for the x ticks
            function rotateXTicks() {
                svg.selectAll('g.x.axis').selectAll('.tick text')
                    .attr("transform",function(d){
                        var t = d3.select(this);
                        var bbox = t.node().getBBox();
                        return "translate("+bbox.height/180*(defaults.labelRotationX%180)+","
                          +Math.abs(bbox.width/170*(defaults.labelRotationX%180))
                          +")rotate("+defaults.labelRotationX+")";})
                    .style("text-anchor","middle");
            }
            rotateXTicks();

            var yAxisEl = svgGroup.select("g.y.axis")
                .transition();

            yAxisEl.call(yAxis);
            if (defaults.guidelinesY) { yAxisEl.call(yGrid); }

            // Enable rotation for the y ticks
            function rotateYTicks() {
                svg.selectAll('g.y.axis').selectAll('.tick text')
                    .attr("transform",function(d){
                        var t = d3.select(this);
                        var bbox = t.node().getBBox();
                        return "translate(" + - Math.abs(bbox.height / 180 * (defaults.labelRotationY % 180)) + ","
                            + bbox.width/90 * (defaults.labelRotationY % 180)
                            + ")rotate(" + defaults.labelRotationY + ")";})
                    .style("text-anchor","end");
            }
            rotateYTicks();

            var text_x =  svgGroup.select("g.x.axis").select("text.x");
            text_x.attr("x", width);
            text_x.attr("y", -6);
            text_x.style("text-anchor", "end");
            text_x.attr("fill", "gray");

            text_x.text(defaults.labelX);

            var text_y = svgGroup.select("g.y.axis").select("text.y");
            text_y.attr("dy", ".71em");
            text_y.attr("y", 6);
            text_y.style("text-anchor", "end");
            text_y.attr("transform", function (d) {
                return "rotate(-90)";
            });
            if (defaults.styles && defaults.styles.labelY){
                text_y.classed(defaults.styles.labelY,true);
            }
            text_y.text(defaults.labelY);

            // Draw line groups
            var lineGroup = svgGroup.selectAll("g.line-group")
                .data(data);

            lineGroup.transition();

            lineGroup.enter().append("g")
                .attr("height",height)
                .attr("width",width)
                .attr("class", function (d,i) {
                    // If there are not enough styles, use the first style.
                    return "line-group " + data[i].key
                    + " " + defaults.styles.classes[i % defaults.styles.classes.length];
                })
                .style("stroke", function (d,i) {
                    return colorScale(i);
                })
                // .style("stroke-width", function(){
                //     return Math.sqrt((height*width))/100+0.5;
                // })
                .append("path").attr("class", "line");

            // Define tip popup
            var tip = d3.tip()
                .attr("class","d3-tip lineChart")
                .offset([-5,0])
                .html( function(d) {
                    var k = defaults.events.xFormat ? defaults.events.xFormat(d.key) : d.key;
                    if (defaults.events && defaults.events.onToolTipShow) {
                        return defaults.events.onToolTipShow(defaults,d,d3.format(defaults.formatTooltipValue)(d.values),k);
                    } else {
                        return "<strong>" +defaults.labelX + " " + k + ":  </strong><br/>" + d3.format(defaults.formatTooltipValue)(d.values);
                    }
                });

            svgGroup.call(tip);

            lineGroup.exit().remove();

            // draw line for each line group
            lineGroup.select("path.line")
                .attr("class", function (d,i) {
                    return defaults.styles.classes[i] + " line";
                })
                .datum(function (d) {
                    return d.values;
                })
                .style("stroke", function (d,i) {
                    return colorScale(i);
                })
                .transition()
                .attr("d", line)
                .style("stroke-width", function(){
                    return Math.sqrt((height*width))/250+0.5;
                });

            // draw circles for each line group
            var circles = lineGroup.selectAll("circle")
                .data(function (d) { return d.values; });

            circles.transition()
                .attr("cy", function (d) {
                    return yScale(d.values);
                })
                .attr("cx", function (d) {
                    return xScale(d.key);
                });

            var onMouseOver = function(d){

                if (defaults.tooltip || defaults.tooltip === undefined){
                    d3.select(this)
                        .attr("fill", function(circle) {
                          return colorScale(circle.index);
                        });
                    tip.show(d);
                }


                if (defaults.events && defaults.events.onMouserOver){
                    defaults.events.onMouseOver(d,d3.select(this));
                }
                d3.event.stopPropagation();
            };
            var onMouseOut = function(d){

                if (defaults.tooltip || defaults.tooltip === undefined){
                    d3.select(this)
                      .attr("fill", "none");
                    tip.hide(d);

                }

                if (defaults.events && defaults.events.onMouseOut){
                    defaults.events.onMouseOut(d,d3.select(this));
                }
                d3.event.stopPropagation();
            };

            circles.enter().append("circle");
            circles.attr("fill", "none")
                .style("stroke", function (d,i) {
                    return colorScale(d.index);
                });

            circles.attr("cy", function (d) {
                return yScale(d.values);
            });
            circles.attr("cx", function (d) {
                return xScale(d.key);
            });

            circles.attr("r", function(){
                    return defaults.circleRadius || Math.sqrt((height*width))/150+0.5;
            });
            circles.style("stroke-width", function(){
                return Math.sqrt((height*width))/300+0.5;
            });
            circles.attr("class", "first");

            circles.on("mouseover",onMouseOver);
            circles.on("mouseout",onMouseOut);
            circles.on("click",function(d){
                if (defaults.events && defaults.events.onDataPointClick){
                    defaults.events.onDataPointClick(d,d3.select(this));
                }
                d3.event.stopPropagation();
            });

            circles.exit().remove();

            // Draw legend
            if (defaults.legend == "bottom") {
                svgGroup.select("g.legend").selectAll("g").remove();
                legend = svgGroup.select("g.legend")
                    .selectAll("g")
                    .data(function () {
                        var arr = [];
                        for (var i = 0; i < data.length; i++) {
                          arr.push(defaults.styles.classes[i%defaults.styles.classes.length]);
                        }
                        return arr;
                    });

                var savedVal = 0;
                var savedLevel = 0;
                var levelDict = {};

                legendItem = legend.enter().append("g")
                    .attr("class", function (d) {
                        return d + " legenditem";
                    });

                legendItem.append("circle")
                    .attr("r", function(){
                            return defaults.circleRadius || Math.sqrt((height*width))/150+0.5;
                    })
                    .attr("class", function (d) {
                        return "legend-" + d;
                    })
                    .attr("fill", "none")
                    .style("stroke", function (d,i) {
                        return colorScale(i);
                    });

                legendItem.append("line")
                    .attr("class", function (d) {
                        return "legend-" + d;
                    })
                    .attr("stroke-width", 1)
                    .attr("stroke", "black")
                    .attr("x1", -13)
                    .attr("x2", 13)
                    .attr("y1", 0)
                    .attr("y2", 0)
                    .style("stroke", function (d,i) {
                        return colorScale(i);
                    });

                legendItem.append("text")
                    .attr("x", 20)
                    .attr("y", 4)
                    .text(function (d, i) {
                        return data[i].key;
                    })
                    .style("opacity", function(d, i) {
                      data[i].textlength = savedVal;
                      data[i].textlevel = savedLevel;
                      savedVal += this.getComputedTextLength() + 50;
                      if (savedVal > width) {
                        levelDict[savedLevel] = (width - data[i].textlength) / 2;
                        // console.log("Reached end of line", levelDict);
                        savedVal = this.getComputedTextLength() + 50;
                        savedLevel += 1;
                        data[i].textlength = 0;
                        data[i].textlevel = savedLevel;
                      }
                      if (i == data.length - 1) {
                        levelDict[savedLevel] = (width - savedVal) / 2;
                        // console.log("Reached end", levelDict);
                      }
                    });

                legend.transition()
                  .duration(0)
                  .attr("transform", function (d, i) {
                      return "translate(" + (data[i].textlength + levelDict[data[i].textlevel]) + "," + (data[i].textlevel * 15) + ")";
                  });

                legend.exit().remove();

                svg.select("g.legend").transition()
                  .duration(0)
                  .attr("transform", function (d, i) {
                      var legendWidth = this.getBBox().width;
                      var xTranslate = (width - legendWidth) / 2;
                      return "translate(0," + (height + 45) + ")";
                  });
              }

            else if (defaults.legend == "right") {
                svgGroup.select("g.legend").selectAll("g").remove();
                legend = svgGroup.select("g.legend")
                .attr("transform", function (d) {
                    return "translate(" + (width + 25) + "," + 25 + ")";
                })
                .selectAll("g")
                .data(function () {
                    var arr = [];
                    for (var i = 0; i < data.length; i++) {
                      arr.push(defaults.styles.classes[i%defaults.styles.classes.length]);
                    }
                    return arr;
                });
                legend.transition();

                legendItem = legend.enter().append("g")
                    .attr("class", function (d) {
                        return d;
                    })
                    .attr("transform", function (d, i) {
                        return "translate(0," + i * 20 + ")";
                    });

                legendItem.append("circle")
                    .attr("r", function(){
                            return defaults.circleRadius || Math.sqrt((height*width))/150+0.5;
                    })
                    .attr("class", function (d) {
                        return "legend-" + d;
                    })
                    .attr("fill", "none")
                    .style("stroke", function (d,i) {
                        return colorScale(i);
                    });

                legendItem.append("line")
                    .attr("class", function (d) {
                        return "legend-" + d;
                    })
                    .attr("stroke-width", 1)
                    .attr("stroke", "black")
                    .attr("x1", -13)
                    .attr("x2", 13)
                    .attr("y1", 0)
                    .attr("y2", 0)
                    .style("stroke", function (d,i) {
                        return colorScale(i);
                    });

                legendItem.append("text")
                    .attr("x", 20)
                    .attr("y", 4)
                    .text(function (d, i) {
                        return data[i].key;
                    });

                    legend.exit().remove();
            }

            function wrap() {
                var self = d3.select(this),
                    textLength = self.node().getComputedTextLength(),
                    text = self.text();
                    var padding = (defaults.margin.left + defaults.margin.right)/2;
                while (textLength > (clientWidth - 2 * padding) && text.length > 0) {
                    text = text.slice(0, -1);
                    self.text(text + '...');
                    textLength = self.node().getComputedTextLength();
                }
            }
            
            if (defaults.hoverLine === true) {
                var hoverTextGroup = svgGroup.append("g").attr("class","hover-text");

                hoverTextGroup.transition();

                var hoverText = hoverTextGroup
                    .append("text")
                    .attr("dy","-0.5em");

                var hoverLineGroup = svgGroup.insert("g","g.chart-area").attr("class","hover-line");

                var hoverLine = hoverLineGroup
                    .append("line")
                        .attr("x1",0).attr("x2",0)
                        .attr("y1",0).attr("y2",height)
                        .style("stroke","gray")
                        .style("stroke-width","1");

                var test_coords = [0, 0];
                var mouseX = test_coords[0];
                var mouseY = test_coords[1];

                // hover line behavior
                function hovering() {
                    test_coords = d3.mouse(this);
                    mouseX = test_coords[0] - defaults.margin.left;
                    mouseY = test_coords[1] - defaults.margin.top;
                    var domain = xScale.domain();
                    var range = xScale.range();

                    var indexX = d3.bisectLeft(range, mouseX) - 1;
                    var keyX = domain[d3.bisectRight(range, mouseX) - 1];

                    if (mouseX >=0 && mouseY >= 0 && mouseX <= width && mouseY <= height) {
                        circles.style('fill', function(d){
                            return d.key === keyX ? colorScale(d.index) : "none";
                        });

                        // hover snapping
                        if (defaults.hoverSnap === true) {
                            snapX = Math.min(width, Math.max(0, xScale(keyX) === undefined ? 0 : xScale(keyX)));
                            hoverLine.attr("x1",snapX).attr("x2",snapX)
                                .style("stroke-width","1");
                        }
                        else {
                            hoverLine.attr("x1",mouseX).attr("x2",mouseX)
                                .style("stroke-width","1");
                        }

                        // hover text
                        hoverText.text(function() {
                            // apply to d3.format of s e.g-".[x]s"
                            var isDirtyFixBytesToMoney = false;
                            if (defaults.formatY.indexOf('s')>-1) {
                              isDirtyFixBytesToMoney = true;
                            }
                            var full_text = '';
                            if (keyX) {
                                full_text= full_text+ " " + (defaults.events.xFormat ?  defaults.events.xFormat(keyX) : keyX) + " | " ;
                            }

                            data.forEach(function(category, i) {

                                category.values.forEach(function(val) {
                                    if (val.key == keyX){
                                        // replacing G with B is a dirty hack as d3 do not have a money scale (but rather a bytes scale). Bytes scale will
                                        // never be needed. So it is probably safe to replace G with B.
                                        if (isDirtyFixBytesToMoney){
                                              full_text = full_text + " " + category.key+ " " + (d3.format(defaults.formatY)(val.values)).replace("G", "B");
                                        }
                                        else {
                                            full_text = full_text + " " + category.key + " " + d3.format(defaults.formatY)(val.values);
                                        }
                                        full_text = full_text + " , ";
                                    }
                                });
                            });
                           full_text= full_text.substr(0,full_text.length-2);
                            if (defaults.events.onHoverLineText){
                                return defaults.events.onHoverLineText(keyX, indexX, data,d3.format(defaults.formatY));
                            }
                            else {
                                return full_text;
                            }
                        })
                        .each(wrap);
                    }
                    else if (defaults.hoverOut){
                        circles.style('fill', function(d){
                            return "none";
                        });
                        hoverLine.attr("x1",0).attr("x2",0)
                            .style("stroke-width","0");
                        hoverText.text("");
                    }
                }
                svg.on('mousemove', hovering);
            }

            if (defaults && defaults.events && defaults.events.onChartReady){
                defaults.events.onChartReady(d3,svg);
            }
        }
    }

    return {
        restrict: 'A',
        replace: true,
        require: "?ngModel",
        transclude: true,
        priority: 1,
        scope: {ngModel:'='},
        template: "<div class='chart line-chart'><svg><g><g class='x axis'><text class='x'></text></g><g class='y axis'><text class='y'></text></g><g class='legend'></g></g></svg></div>",
        link: function(scope, element, attrs,ngModelCtrl,transclude) {
            var original_template = element[0].innerHTML;

            // called when ng-model in its entirety changes (re-assigned)
            if (ngModelCtrl){
                $timeout(function(){
                    ngModelCtrl.$render = function(){
                        element[0].innerHTML = original_template;
                        renderChart(element,attrs,ngModelCtrl.$viewValue);
                    };
                });
            }

            // called when the directive is first loaded
            transclude(function(clonedEl){
                if (ngModelCtrl){
                    $timeout(function(){
                        element[0].innerHTML = original_template;
                        renderChart(element,attrs,ngModelCtrl.$viewValue);
                    });
                }
            });

            // called when any of the properties are changed
            scope.$watch(function() { return ngModelCtrl.$viewValue; }, function(oldVal, newVal) {
                if (oldVal != newVal) {
                    element[0].innerHTML = original_template;
                    renderChart(element,attrs,ngModelCtrl.$viewValue);
                }
            }, true);

            // support window resizing
            angular.element($window).bind('resize', function() {
                element[0].innerHTML = original_template;
                renderChart(element,attrs,ngModelCtrl.$viewValue);
            });
        }
    };
}]);