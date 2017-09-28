using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.Mvc;
using UserHits.Models;

namespace UserHits.Controllers
{
    public class HomeController : Controller
    {
        public JsonResult GetLastVisitedPage(List<Hit> hits)
        {
            try
            {
                // group hits by UserId
                var grouped = hits.GroupBy(hit => hit.UserId);

                // order each group by Date and get latest one
                var mostRecent = grouped.Select(group => group.OrderBy(hit => hit.Date).Last());
                return Json(mostRecent);
            }
            catch (Exception e)
            {
                return Json(null);
            }
        }

        public JsonResult GetTopUsers(List<User> users, List<Hit> hits, int count)
        {
            try
            {
                // group hits by UserId
                var grouped = hits.GroupBy(hit => hit.UserId);

                // order each group by count and take top X, where X = count
                var top = grouped.OrderByDescending(group => group.Count()).Take(count);

                // select only the Hit object from each grouping of <Guid, Hit>
                var listOfHits = top.Select(group => group.Last());

                // join users to hits to get list of users
                var result = from u in users
                             join h in listOfHits on u.Id equals h.UserId
                             select u;

                return Json(result);
            }
            catch (Exception e)
            {
                return Json(null);
            }
        }
    }
}