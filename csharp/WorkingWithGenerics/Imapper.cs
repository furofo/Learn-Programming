namespace Essentials2Library
{
    public interface IMapper<S, T>
    {
        // source is object or type we put in target is object or type we want
        T Map(S source);

    }
}