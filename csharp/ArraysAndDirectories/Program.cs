// string[] names = new string[2];
// names[0] = "John";
// names[1] = "Doe";
// Console.WriteLine("Hello {0} {1}", names);

var al = new System.Collections.ArrayList(2);
al.Add("John");
al.Add("Doe");
al.AddRange(new string[] { "Jane", "Smith" });
Console.WriteLine("Hello {0} {1} {2}, {3}", al[0], al[1], al[2], al[3]);
Console.WriteLine($"The ArrayList size is is {al.Count}");
Console.WriteLine("Indexed item from collection [2]: {0}", al[2]);
Console.WriteLine("All items in the list:");
foreach (var item in al)
{
    Console.WriteLine(item);
}