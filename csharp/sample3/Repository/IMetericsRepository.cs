using System.Collections.Generic;
using Question2.Models;

namespace Question2.Repository
{
    public interface IMetericsRepository
    {
        IList<UserStats> GetTopNUsers(int topNum);

        IList<Hit> GetLastVisitedPageByUsers();
    }
}