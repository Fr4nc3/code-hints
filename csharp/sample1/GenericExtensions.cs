
namespace Msft.Extensions
{
    // custom extension class for In and Pos methods
    public static class GenericExtensions
    {
        public static bool In<T>(this T obj, params T[] array)
        {
            foreach (var item in array)
            {
                if (obj.Equals(item))
                {
                    return true;
                }
            }

            return false;
        }

        public static int Pos<T>(this T obj, params T[] array)
        {
            for (var i = 0; i < array.Length; i++)
            {
                if (obj.Equals(array[i]))
                {
                    return i;
                }
            }

            return -1;
        }
    }
}
