using System.Web.Mvc;
using Question2.Repository;

namespace Question2.Controllers
{

    //[Authorize]
    public class MetericController : Controller
    {

        IMetericsRepository _metricsRepo = null;

        public MetericController()
        {
            _metricsRepo = new MetericsRepository();
        }

        /// <summary>
        /// This constructor can be used for Dependency Injection or
        /// for testing to inject fake repository
        /// </summary>
        /// <param name="metricsRepo"></param>
        public MetericController(IMetericsRepository metricsRepo)
        {
            _metricsRepo = metricsRepo;
        }
        /// <summary>
        /// Get Top 'N' Users
        /// </summary>
        /// <param name="topNum"></param>
        /// <returns></returns>
        [Route("meteric/top/{topNum:int}/users")]
        public ActionResult GetTopNUsers(int topNum)
        {
            if (topNum <= 0) topNum = 10;
            var result = _metricsRepo.GetTopNUsers(topNum);

            return Json(result, JsonRequestBehavior.AllowGet);
        }


        /// <summary>
        /// Get Last Visited Page by user
        /// </summary>
        /// <returns></returns>
        [Route("meteric/lastvistedpagebyusers")]
        public ActionResult GetLastVisitedPageByUsers()
        {
            var result = _metricsRepo.GetLastVisitedPageByUsers();

            return Json(result, JsonRequestBehavior.AllowGet);
        }
    }
}