using System;
using System.Runtime.CompilerServices;

public class Person
{
    public string Name { get; set; } = string.Empty;
    public int Age { get; set; }
    public int Id { get; set; }
}

class Program
{
    static void Main()
    {
        Person person1 = new Person { Name = "Alice", Age = 25, Id = 1 };
        Person person2 = new Person { Name = "Bob", Age = 30, Id = 2 };
        Person person3 = person1; // person3 references the same instance as person1
        Person person4 = new Person { Name = "Alice", Age = 25, Id = 1 };

        Console.WriteLine($"person1 and person2 are the same instance: {ReferenceEquals(person1, person2)}");
        Console.WriteLine($"person1 and person3 are the same instance: {ReferenceEquals(person1, person3)}");
        Console.WriteLine($"person1 and person4 are the same instance: {ReferenceEquals(person1, person4)}");

        Console.WriteLine($"Hash code of person1: {GetObjectHashCode(person1)}");
        Console.WriteLine($"Hash code of person2: {GetObjectHashCode(person2)}");
        Console.WriteLine($"Hash code of person3: {GetObjectHashCode(person3)}");
        Console.WriteLine($"Hash code of person4: {GetObjectHashCode(person4)}");
    }

    static int GetObjectHashCode(object obj)
    {
        return RuntimeHelpers.GetHashCode(obj);
    }
}