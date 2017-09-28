using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

/// <summary>
/// pseudo code for get active page visits statics
/// </summary>
public class VisitStatController : ApiController
{
        List<Hit> hits = new List<Hit>() { ... };
        List<User> users = new List<User>() { ... };


        [Route("/visitedpages")]
        [HttpGet]
        public IHttpActionResult LastdayAllPages()
        {
            if (hits == null || users == null)
                new HttpResponseException(
                    new HttpResponseMessage(HttpStatusCode.InternalServerError)
                    {
                        Content = new StringContent("hits data is not existing"),
                        ReasonPhrase = "No Hits Data"
                    });

            var lastDayHitByUser = hits.AsEnumerable<Hit>()
                .Where(hit => hit.Date >= DateTime.Today.AddDays(-1) && hit.Date < DateTime.Today)
                .GroupBy(hit => hit.UserId).SelectMany(grp => grp.OrderByDescending(userHits => userHits.Date).Take(1))
                .OrderBy(hit => hit.UserId)
                .Select(hit => new { User = hit.UserId, Url = hit.Url });
            return Ok(lastDayHitByUser);
        }

        [Route("/activeusers")]
        [HttpGet]
        public IHttpActionResult MostActiveUser()
        {
            if (hits == null || users == null)
                new HttpResponseException(
                    new HttpResponseMessage(HttpStatusCode.InternalServerError)
                    {
                        Content = new StringContent("hits data is not existing"),
                        ReasonPhrase = "No Hits Data"
                    });

            var activeUsers = hits.AsEnumerable<Hit>().GroupBy(hit => hit.UserId)
                .Select(grp => new { UserId = grp.Key, AllVisits = grp.Count() })
                .OrderByDescending(visits => visits.AllVisits).Take(10)
                .Join(users, visits => visits.UserId, user => user.Id
                    , (visits, user) => new { UId = user.Id, Name = user.FirstName + " " + user.LastName, Visits = visits.AllVisits });
            return Ok(activeUsers);
        }
}
