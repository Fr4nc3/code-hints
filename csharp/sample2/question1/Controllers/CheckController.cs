using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Security.Cryptography;
using System.Web;
using System.Web.Mvc;
using Assignment.Models;

namespace Assignment.Controllers
{
    public class CheckController : Controller
    {
        // GET: Check
        /// <summary>
        /// Index Method which loads Index View
        /// </summary>
        /// <returns>View</returns>
        public ActionResult Index()
        {         
            return View();
        }

        /// <summary>
        /// ActiveUsers() will write Top 10 most active users anytime
        /// </summary>
        /// <returns> collection of Hits objects</returns>
        [HttpGet]
        public ActionResult ActiveUers()
        {
            List<User> users = new List<User>();
             List<Hit> hits = new List<Hit>();
        
            Guid a = Guid.NewGuid();
            Guid b = Guid.NewGuid();
            Guid c = Guid.NewGuid();
            Guid d = Guid.NewGuid();
            Guid e = Guid.NewGuid();
            Guid f = Guid.NewGuid();
            Guid g = Guid.NewGuid();
            Guid i = Guid.NewGuid();
            Guid j = Guid.NewGuid();
            Guid k = Guid.NewGuid();
            Guid l = Guid.NewGuid();
            Guid m = Guid.NewGuid();
            Guid n = Guid.NewGuid();
            Guid o = Guid.NewGuid();
            Guid p = Guid.NewGuid();
            Guid q = Guid.NewGuid();
            users.Add(new User() {Id = a, FirstName = "Sara", LastName = "S"});
            users.Add(new User() { Id = b, FirstName = "Sara", LastName = "S" });
            users.Add(new User() { Id = c, FirstName = "Jesse", LastName = "Ross" });
            users.Add(new User() { Id = d, FirstName = "Scott", LastName = "Green" });
            users.Add(new User() { Id = e, FirstName = "Jason", LastName = "Harris" });
            users.Add(new User() { Id = f, FirstName = "Chandra", LastName = "gotta" });
            users.Add(new User() { Id = g, FirstName = "Sharon", LastName = "Brown" });
            users.Add(new User() { Id = i, FirstName = "satish", LastName = "Manchi" });
            users.Add(new User() { Id = j, FirstName = "laxmi", LastName = "manchu" });
            users.Add(new User() { Id = k, FirstName = "Jason", LastName = "Vallc" });
            users.Add(new User() { Id = l, FirstName = "milind", LastName = "Vakendi" });
            users.Add(new User() { Id = m, FirstName = "Jim", LastName = "Fisher" });
            users.Add(new User() { Id = n, FirstName = "yan", LastName = "chiop" });
            users.Add(new User() { Id = o, FirstName = "Julie", LastName = "yung" });
            users.Add(new User() { Id = p, FirstName = "Joel", LastName = "Richart" });
            users.Add(new User() { Id = q, FirstName = "brandsy", LastName = "byrxt" });


            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = a, Url = "www.abc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = b, Url = "www.xyz.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = c, Url = "www.apaybc.com", Date = DateTime.Today.AddDays(-1) });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = d, Url = "www.abc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = e, Url = "www.bbsbx.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = f, Url = "www.asxsbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = g, Url = "www.ssdsdssas.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = i, Url = "www.asdsdbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = j, Url = "www.absddbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = k, Url = "www.sdsdabc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = l, Url = "www.asdsdbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = m, Url = "www.asssbc.com", Date = DateTime.Now });
            hits.Add(new Hit() {Id = Guid.NewGuid(), UserId = n, Url = "www.sssss.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = o, Url = "www.abhjbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = p, Url = "www.gghjj.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = q, Url = "www.ghhuui.com", Date = DateTime.Now });
            hits.Add(new Hit() {Id = Guid.NewGuid(), UserId = a, Url = "www.gghjuj.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = b, Url = "www.vggyu.com", Date = DateTime.Today.AddDays(-1) });
            hits.Add(new Hit() {Id = Guid.NewGuid(), UserId = c, Url = "www.ffyuhu.com", Date = DateTime.Today.AddDays(-1) });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = d, Url = "www.abc.com", Date = DateTime.Now });

            var res = from h in hits
                join u in users on h.UserId equals u.Id
                orderby h.Url.Count() descending
                select(
                    new ActiveUersViewModel()
                    {
                        FirstName = u.FirstName,
                        Date = h.Date,
                        Id = h.UserId,
                        LastName = u.LastName,
                        Url = h.Url
                    });
            return View(res.ToList().Distinct().Take(10));

        }

        /// <summary>
        /// LastVisitedUsers() will write Last visited page yesterday for each user
        /// </summary>
        /// <returns> collection of Hitsts objects</returns>
        [HttpGet]
        public ActionResult LastVisitedUsers()
        {
            //Assuming, we are not having any database, intializing the data
            List<User> users = new List<User>();
            List<Hit> hits = new List<Hit>();

            Guid a = Guid.NewGuid();
            Guid b = Guid.NewGuid();
            Guid c = Guid.NewGuid();
            Guid d = Guid.NewGuid();
            Guid e = Guid.NewGuid();
            Guid f = Guid.NewGuid();
            Guid g = Guid.NewGuid();
            Guid i = Guid.NewGuid();
            Guid j = Guid.NewGuid();
            Guid k = Guid.NewGuid();
            Guid l = Guid.NewGuid();
            Guid m = Guid.NewGuid();
            Guid n = Guid.NewGuid();
            Guid o = Guid.NewGuid();
            Guid p = Guid.NewGuid();
            Guid q = Guid.NewGuid();
            users.Add(new User() { Id = a, FirstName = "Sara", LastName = "S" });
            users.Add(new User() { Id = b, FirstName = "Sara", LastName = "S" });
            users.Add(new User() { Id = c, FirstName = "Jesse", LastName = "Ross" });
            users.Add(new User() { Id = d, FirstName = "Scott", LastName = "Green" });
            users.Add(new User() { Id = e, FirstName = "Jason", LastName = "Harris" });
            users.Add(new User() { Id = f, FirstName = "Chandra", LastName = "gotta" });
            users.Add(new User() { Id = g, FirstName = "Sharon", LastName = "Brown" });
            users.Add(new User() { Id = i, FirstName = "satish", LastName = "Manchi" });
            users.Add(new User() { Id = j, FirstName = "laxmi", LastName = "manchu" });
            users.Add(new User() { Id = k, FirstName = "Jason", LastName = "Vallc" });
            users.Add(new User() { Id = l, FirstName = "milind", LastName = "Vakendi" });
            users.Add(new User() { Id = m, FirstName = "Jim", LastName = "Fisher" });
            users.Add(new User() { Id = n, FirstName = "yan", LastName = "chiop" });
            users.Add(new User() { Id = o, FirstName = "Julie", LastName = "yung" });
            users.Add(new User() { Id = p, FirstName = "Joel", LastName = "Richart" });
            users.Add(new User() { Id = q, FirstName = "brandsy", LastName = "byrxt" });


            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = a, Url = "www.abc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = b, Url = "www.xyz.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = c, Url = "www.apaybc.com", Date = DateTime.Today.AddDays(-1) });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = d, Url = "www.abc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = e, Url = "www.bbsbx.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = f, Url = "www.asxsbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = g, Url = "www.ssdsdssas.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = i, Url = "www.asdsdbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = j, Url = "www.absddbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = k, Url = "www.sdsdabc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = l, Url = "www.asdsdbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = m, Url = "www.asssbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = n, Url = "www.sssss.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = o, Url = "www.abhjbc.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = p, Url = "www.gghjj.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = q, Url = "www.ghhuui.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = a, Url = "www.gghjuj.com", Date = DateTime.Now });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = b, Url = "www.vggyu.com", Date = DateTime.Today.AddDays(-1) });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = c, Url = "www.ffyuhu.com", Date = DateTime.Today.AddDays(-1) });
            hits.Add(new Hit() { Id = Guid.NewGuid(), UserId = d, Url = "www.abc.com", Date = DateTime.Now });


                  var res = from h in hits
                      join u in users on h.UserId equals u.Id
                      where h.Date == DateTime.Today.AddDays(-1)  
                      orderby h.Date descending
                      select (
                          new ActiveUersViewModel()
                          {
                              FirstName = u.FirstName,
                              Date = h.Date,
                              Id = h.UserId,
                              LastName = u.LastName,
                              Url = h.Url
                          });
                        
            return View(res.GroupBy(pm => pm.Id).SelectMany(gp => gp.OrderByDescending(pm => pm.Date).Take(1)));

        }

  
    }
}