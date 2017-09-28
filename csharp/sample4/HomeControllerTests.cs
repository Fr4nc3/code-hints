using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using UserHits.Models;
using System.Web.Mvc;

namespace UserHits.Controllers.Tests
{
    [TestClass()]
    public class HomeControllerTests
    {
        [TestMethod()]
        public void GetLastVisitedPageTest()
        {
            HomeController controller = new HomeController();

            List<User> users = new List<User>();

            User one = new User()
            {
                Id = Guid.NewGuid(),
                FirstName = "Leszek",
                LastName = "Zychowski"
            };

            User two = new User()
            {
                Id = Guid.NewGuid(),
                FirstName = "Bob",
                LastName = "Smith"
            };

            users.Add(one);
            users.Add(two);

            List<Hit> hits = new List<Hit>();

            Hit first = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = one.Id,
                Url = "http://www.bing.com/",
                Date = Convert.ToDateTime("08/23/2016 13:51:00.00")
            };

            Hit second = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = one.Id,
                Url = "http://www.msn.com/",
                Date = Convert.ToDateTime("08/22/2016 13:51:00.00")
            };

            Hit third = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = one.Id,
                Url = "http://www.msdn.com/",
                Date = Convert.ToDateTime("08/21/2016 13:51:00.00")
            };

            Hit fourth = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = two.Id,
                Url = "http://www.msn.com/",
                Date = Convert.ToDateTime("07/22/2016 13:51:00.00")
            };

            Hit fifth = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = two.Id,
                Url = "http://www.msdn.com/",
                Date = Convert.ToDateTime("07/21/2016 13:51:00.00")
            };

            hits.Add(first);
            hits.Add(second);
            hits.Add(third);
            hits.Add(fourth);
            hits.Add(fifth);

            JsonResult pages = controller.GetLastVisitedPage(hits);

            var data = (IEnumerable<Hit>)pages.Data;

            Assert.IsNotNull(pages);
            Assert.AreEqual(DateTime.Parse("08/23/2016 13:51:00.00"), data.First().Date);
        }

        [TestMethod()]
        public void GetTopUsersTest()
        {
            HomeController controller = new HomeController();

            // create users

            List<User> users = new List<User>();

            User one = new User()
            {
                Id = Guid.NewGuid(),
                FirstName = "Leszek",
                LastName = "Zychowski"
            };

            User two = new User()
            {
                Id = Guid.NewGuid(),
                FirstName = "Bob",
                LastName = "Smith"
            };

            User three = new User()
            {
                Id = Guid.NewGuid(),
                FirstName = "John",
                LastName = "Doe"
            };

            users.Add(one);
            users.Add(two);
            users.Add(three);

            // create hits

            List<Hit> hits = new List<Hit>();

            Hit first = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = one.Id,
                Url = "http://www.bing.com/",
                Date = Convert.ToDateTime("08/23/2016 13:51:00.00")
            };

            Hit second = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = one.Id,
                Url = "http://www.msn.com/",
                Date = Convert.ToDateTime("08/22/2016 13:51:00.00")
            };

            Hit third = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = one.Id,
                Url = "http://www.msdn.com/",
                Date = Convert.ToDateTime("08/21/2016 13:51:00.00")
            };

            Hit fourth = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = two.Id,
                Url = "http://www.msn.com/",
                Date = Convert.ToDateTime("07/22/2016 13:51:00.00")
            };

            Hit fifth = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = two.Id,
                Url = "http://www.msdn.com/",
                Date = Convert.ToDateTime("07/21/2016 13:51:00.00")
            };

            Hit sixth = new Hit()
            {
                Id = Guid.NewGuid(),
                UserId = three.Id,
                Url = "http://www.msdn.com/",
                Date = Convert.ToDateTime("07/21/2016 13:51:00.00")
            };

            hits.Add(fourth);
            hits.Add(fifth);
            hits.Add(first);
            hits.Add(second);
            hits.Add(third);
            hits.Add(sixth);

            // call controller

            JsonResult topUsers = controller.GetTopUsers(users, hits, 10);

            var data = (IEnumerable<User>)topUsers.Data;

            Assert.IsNotNull(users);
            Assert.AreEqual("Leszek", data.First().FirstName);
        }
    }
}