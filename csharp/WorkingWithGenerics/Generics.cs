using System;
using System.Runtime.CompilerServices;

string jsonPerson = "{\"Name\":\"Green\",\"Age\":25,\"Id\":1}";
// deseralize json to object
var pj = System.Text.Json.JsonSerializer.Deserialize<Person>(jsonPerson);
Console.WriteLine($"{pj?.Name} is a json persons");

static void Swap<T>(ref T a, ref T b)
{
    T temp = a;
    a = b;
    b = temp;
}

Nullable<int> x = 7;
Nullable<DateTime> maybeDate = null;
//maybeDate = DateTime.Now;
Console.WriteLine($"maybeDate: {maybeDate}");
public class Person
{
    public string Name { get; set; } = string.Empty;
    public int Age { get; set; }
    public int Id { get; set; }
}
