int x = 5, y = 7;
Console.WriteLine($"Before: x = {x}, y = {y}");
Swap(x, y);
Console.WriteLine($"After: x = {x}, y = {y}");
static void Swap(object first, object second)
{
    object temp = first;
    first = second;
    second = temp;
}