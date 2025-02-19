using System;
using System.Runtime.CompilerServices;

Person person1 = new Person { Name = "Alice", Age = 25, Id = 1 };
Person person2 = new Person { Name = "Bob", Age = 30, Id = 2 };

Console.WriteLine($"Before swap: {person1.Name}, {person2.Name}");
Swap(ref person1, ref person2);
Console.WriteLine($"After swap: {person1.Name}, {person2.Name}");


static void Swap(ref object a, ref object b)
{
    object temp = a;
    a = b;
    b = temp;
}

public class Person
{
    public string Name { get; set; } = string.Empty;
    public int Age { get; set; }
    public int Id { get; set; }
}
