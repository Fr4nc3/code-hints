public static class SearchExtensions
{
    public static bool In<T>(this T Source, params T[] SearchList)
    {
        if (((object)Source) == null)
            return false;
        foreach (T elem in SearchList)
            if (Source.Equals(elem))
                return true;
            else
                continue;
        return false;
    }

    /// <summary>
    /// 
    /// </summary>
    /// <typeparam name="T"></typeparam>
    /// <param name="Source">Element to search</param>
    /// <param name="SearchList"></param>
    /// <returns>-1: not in the list; otherwise the 1-based position</returns>
    public static int Pos<T>(this T Source, params T[] SearchList)
    {
        if (((object)Source) == null || SearchList.Length == 0)
            return -1;

        for (int i = 0; i < SearchList.Length; i++)
            if (Source.Equals(SearchList[i]))
                return i + 1;
            else
                continue;
        return -1;
    }
}
