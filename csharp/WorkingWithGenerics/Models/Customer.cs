namespace WorkingWithGenerics.Models
{
    public class Customer
    {
        public string Name { get; set; } = string.Empty;
        public int Age { get; set; }
        public int Id { get; set; }
        public DateOnly CreateDate { get; set; }

    }

}