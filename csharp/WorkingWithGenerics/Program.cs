using WorkingWithGenerics.Models;
using WorkingWithGenerics.Mappers;

var c = new Customer
{
    Id = 1,
    Name = "John Doe who used to be Customer",
    Age = 30,
    CreateDate = new DateOnly(2021, 10, 1)
};

var p = new Person
{
    Id = 1,
    Name = "John Doe Person",
    Age = 30
};

var mapper = new CustomerToPersonMapper();
var person = mapper.Map(c);
Console.WriteLine($"Person: {person.Name}");