using Essentials2Library;
using WorkingWithGenerics.Models;

class PersonToCustomerMapper : IMapper<Person, Customer>
{
    public Customer Map(Person source)
    {
        return new Customer(source.Age, source.Id, source.Name);
    }



}