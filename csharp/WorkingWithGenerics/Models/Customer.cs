namespace WorkingWithGenerics.Models
{
    public class Customer
    {
        public string Name { get; set; } = string.Empty;
        public int Age { get; set; }
        public int Id { get; set; }
        public DateOnly CreateDate { get; set; }

        // Custom constructor that requires Age and Id
        public Customer(int age, int id, string name)
        {
            Age = age;
            Id = id;
            CreateDate = DateOnly.FromDateTime(DateTime.Now); // Example of setting a default value
            Name = name;
        }
    }
}