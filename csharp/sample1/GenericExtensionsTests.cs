

using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Msft.Extensions.Tests
{
    [TestClass()]
    public class GenericExtensionsTests
    {
        // In() tests

        [TestMethod()]
        public void InTestFound()
        {
            var myFruit = MyFruitEnum.Orange;
            var myFruitFound = myFruit.In(MyFruitEnum.Orange, MyFruitEnum.Banana);

            Assert.IsTrue(myFruitFound);
        }

        [TestMethod()]
        public void InTestNotFound()
        {
            var myString = "vvv";
            var myStringFound = myString.In("foo", "bar", "baz", "qux");

            Assert.IsFalse(myStringFound);
        }

        // Pos() tests

        [TestMethod()]
        public void PosFound()
        {
            var myInt = 8;
            var indexOfMyInt = myInt.Pos(3, 8, 11, 9);

            Assert.AreEqual(indexOfMyInt, 1);
        }

        // if letter is not found, return -1 

        [TestMethod()]
        public void PosNotFound()
        {
            var myChar = 'v';
            var indexOfMyChar = myChar.Pos('x', 'y', 'z');

            Assert.AreEqual(indexOfMyChar, -1);
        }
    }
}