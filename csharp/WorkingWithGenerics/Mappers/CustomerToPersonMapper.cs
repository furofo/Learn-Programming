using Essentials2Library;
using WorkingWithGenerics.Models;

namespace WorkingWithGenerics.Mappers
{
    public class CustomerToPersonMapper : IMapper<Customer, Person>
    {
        public Person Map(Customer source)
        {
            return new Person
            {
                Id = source.Id,
                Name = source.Name,
            };
        }
    }
}