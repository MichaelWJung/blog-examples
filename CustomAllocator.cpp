#include <cstdlib>
#include <functional>
#include <iostream>
#include <list>
#include <set>
#include <typeinfo>
#include <vector>

template<class T>
class MyAllocator
{
public:
    typedef T value_type;

    MyAllocator() : state(0) {}
    explicit MyAllocator(int state) : state(state) {}

    template<class U>
    MyAllocator(const MyAllocator<U>& other)
        : state(other.state) {}
    template<class U>
    MyAllocator(MyAllocator<U>&& other)
        : state(other.state) {}

    template<class U>
    MyAllocator& operator=(const MyAllocator<U>& other)
    {
        state = other.state;
    }
    template<class U>
    MyAllocator& operator=(MyAllocator<U>&& other)
    {
        state = other.state;
    }

    T* allocate(size_t n)
    {
        std::cout << "Allocate " << n * sizeof(T)
                  << " bytes (type "
                  << typeid(T).name() << ")." << std::endl;
        return static_cast<T*>(std::malloc(n * sizeof(T)));
    }

    void deallocate(T* ptr, size_t n)
    {
        std::cout << "Deallocate " << n * sizeof(T)
                  << " bytes at " << ptr << " (type "
                  << typeid(T).name() << ")." << std::endl;
        std::free(ptr);
    }

    template<class U>
    bool operator==(const MyAllocator<U>& other)
    {
        return state == other.state;
    }

    template<class U>
    bool operator!=(const MyAllocator<U>& other)
    {
        return !(*this == other);
    }

private:
    int state;
};

template<class T>
using MyVector = std::vector<T, MyAllocator<T>>;

template<class T>
using MyList = std::list<T, MyAllocator<T>>;

template<class Key, class Compare = std::less<Key>>
using MySet = std::set<Key, Compare, MyAllocator<Key>>;

class Foo
{
public:
    explicit Foo(int i = 0) : i(i) {}
    bool operator<(const Foo& other) const
    {
        return i < other.i;
    }

private:
    int i;
};

int main()
{
    std::cout << "MyVector:" << std::endl;
    {
        MyVector<Foo> vec;
        for (size_t i = 0; i < 100; ++i)
            vec.push_back(Foo());
    }

    std::cout << "\nMyList:" << std::endl;
    {
        MyList<Foo> list;
        for (size_t i = 0; i < 5; ++i)
            list.push_back(Foo());
    }

    std::cout << "\nMySet:" << std::endl;
    {
        MySet<Foo> set;
        for (size_t i = 0; i < 5; ++i)
            set.insert(Foo(i));
    }
}
