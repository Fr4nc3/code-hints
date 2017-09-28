using System;


namespace Question2.Models
{
    public class Hit
    {
        public Guid Id { get; set; }
        public Guid UserId { get; set; }
        public string Url { get; set; }
        public DateTime Date { get; set; }
    }  

}