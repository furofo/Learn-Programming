using Essentials2Library;

public class Answer
{
    public static Boolean ShowExpectedResult = false;
    public static Boolean ShowHints = false;

    public static int FindLargest<T>(int[] numbers, T classWithFindLargest) where T : ISolver, new()
    {
        return classWithFindLargest.FindLargest(numbers);
    }
}