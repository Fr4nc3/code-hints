using System;
using System.Collections.Generic;
using System.Linq;
using Question2.Models;

namespace Question2.Repository
{
    public class MetericsRepository : IMetericsRepository
    {

        private List<Hit> _hits = new List<Hit>();
        private List<User> _users = new List<User>();
        public MetericsRepository()
        {
            LoadDummyData();
        }

        /// <summary>
        /// Get last Page visted by all the users yesterday
        /// </summary>
        /// <returns></returns>
        public IList<Hit> GetLastVisitedPageByUsers()
        {
            var dateToday = DateTime.Now;
            var result = _hits
                .Where(c => c.Date >= dateToday.AddDays(-1) && c.Date < dateToday)
                .GroupBy(x => x.UserId, (key, g) => g.OrderByDescending(e => e.Date).First());

            return result.ToList();
        }

        /// <summary>
        /// Get Top 'N' active users
        /// </summary>
        /// <param name="topNum"></param>
        /// <returns></returns>
        public IList<UserStats> GetTopNUsers(int topNum)
        {
            var result = _hits.GroupBy(info => info.UserId)
                        .Select(group => new UserStats
                        {
                            UserId = group.Key,
                            HitCount = group.Count()
                        })
                        .OrderByDescending(x => x.HitCount).Take(topNum);

            return result.ToList();
        }

        /// <summary>
        /// Load Dummy Data, otherwise this will come from DB us
        /// </summary>
        public void LoadDummyData()
        {
            //populate users
            for (int i = 1; i <= 20; i++)
            {
                _users.Add(new User { Id = Guid.NewGuid(), FirstName = "User" + i });
            }

            var random = new Random(10);

            //populate hits for users
            foreach (var user in _users)
            {
                var count = random.Next(10);
                for (int i = 1; i <= count; i++)
                {
                    _hits.Add(new Hit { Id = Guid.NewGuid(), Date = DateTime.Now.Date, UserId = user.Id, Url = string.Format("http://www.test{0}.com", i) });
                }
            }
        }
    }
}