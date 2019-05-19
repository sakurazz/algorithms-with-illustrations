# Unicode 
 
![unicode](https://i.imgur.com/PPzVl82.png)
 

> It does not make sense to have a string without knowing what encoding it uses.  
> 
> by [Joel](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)


## Why？

- **ASCII**: To represent english words but we have other language
- **Code Page**: To support different language but hwo do we communicate with other people speaking different language
- **Unicode**: To enables the exchange of text data internationally
- **Encoding**: To save space 


## How: best practice?

* **Document** character set, character encoding information when introducing new string type data into the system
* At the data entry point of the system, **identify** the character set and encoding of string type data and convert it to UTF-8 if it is not UTF-8 encoded
* Be mindful of the character **encoding** of string type data before processing it
* Passwords should be **ASCII** only
* **Always send UTF-8 encoded Unicode** string between components
* Always **use UTF-8 encoded Unicode string** for hashing

## What?

- **Character Set**: A collection of characters. e.g. GB2312, GBK, UCS, Unicode.
- All the Unicode supported characters are grouped into sections called [**scripts**](https://www.wikiwand.com/en/Script_(Unicode)).
- [**Unicode**](https://www.wikiwand.com/en/Unicode) is an industry standard for consistent encoding of **written text**.
	- The Unicode codespace is divided into seventeen `planes`, numbered 0 to 16. 
	- The Plane 0(0000-FFFF) is called `BMP`(Basic Multilingual Plane). The first 65,536 code points contains the majority of the common characters used in the major languages of the world.  
- **code Point**: The ID of a character in Unicode.
	* "A": `U+0041`
	* "人": `U+4EBA`
- **Character Encoding**: Mapping the characters (code points) to unique code unit sequences. e.g. UTF-8, UTF-16, UTF-32, cp936
- **Code Pages**: A series of legacy character encodings that were invented before the introduction of Unicode. Each code page only works for a character set of a particular language. Different code pages map the same byte sequence into different characters in different character sets. e.g. cp936 for GBK
- **The Unicode Standard** defines a consistent way of encoding multilingual text that enables the exchange of text data internationally and creates the foundation for global software.

### UTF-8, UTF-16, UTF-32

#### UTF-8

```text
    Code point range   |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

A variable width character encoding capable of encoding all code points in Unicode using one to four bytes.

* The first octet of a multi-octet sequence indicates the number of octets in the sequence

**Pros:** 

* The **Boyer-Moore** fast search algorithm can be used with UTF-8 data
* UTF-8 strings can be fairly reliably recognized as such by a simple algorithm
* **ASCII** string is also a valid UTF-8 string
* **ASCII** octet values do not appear otherwise in a UTF-8 encoded character stream



#### UTF-16


```text
   U =  xxxxxxxxxxxxxxxx

   V' = zzzzzzzzzzyyyyyyyyyy
   W1 = 110110zzzzzzzzzz
   W2 = 110111yyyyyyyyyy
```

A character encoding optimized for BMP: all characters in BMP are encoded in exactly two bytes, and all other characters are encoded in exactly four bytes.

Pros:

* UTF-16 may be a preferred encoding form in many environments that need to balance **efficient** access to characters with economical use of **storage**

Cons:

* **Incompatible** with ASCII
* The Boyer-Moore fast search algorithm *cannot* be used with UTF-16 data
* **Endianess** has to be taken into consideration when decoding UTF-16 data


#### UTF-32

The simplest Unicode encoding form: Each Unicode code point is represented directly by a single 32-bit code unit.

**Pros:**

* UTF-32 may be a preferred encoding form where memory or disk storage space for characters is not a particular concern, but where fixed-width, **single code unit access** to characters is desired
* UTF-32 is also a preferred encoding form for processing characters on most **Unix** platforms

**Cons:**

* Incompatible with ASCII
* The Boyer-Moore fast search algorithm *cannot* be used with UTF-16 data

### Language Support 

### Go
```go
    "ÿ"             // UTF-8
    "\xc3\xbf"
    "\u00FF"        // UTF-16
    "\U000000FF"    // UTF-32
```

* Go source code is always UTF-8.
* A string holds arbitrary bytes.
* A string literal, absent byte-level escapes, always holds valid UTF-8 sequences.
* Those sequences represent Unicode code points, called runes.
* No guarantee is made in Go that characters in strings are normalized.

Besides the axiomatic detail that Go source code is UTF-8, there's really only one way that Go treats UTF-8 specially, and that is when using a for range loop on a string, which decodes one UTF-8-encoded rune on each iteration.

```go
    for index, runeValue := range str {
        fmt.Printf("%#U starts at byte position %d\n", runeValue, index)
    }
```

The most important package for UTF-8 support is `unicode/utf8`, which contains helper routines to validate, disassemble, and reassemble UTF-8 strings.

```go
    length = utf8.RuneCountInString(str)
    runes := []rune(str)
    var strInUTF16 []uint16 = utf16.Encode(runes)
    var codePoint rune = '⌘'
    isContain := strings.ContainRune(str, codePoint)
    index := strings.IndexRune(str, codePoint)
```

### C++
```cpp
    std::string asciiStr = "Narrow multibyte string literal"
    std::u16string utf16Str = u"UTF-16字符串常量"
    std::u32string utf32Str = U"UTF-32字符串常量"

    std::string utf8Str = "\u591a\U00005b57\xe8\x8a\x82码"
    std::u16string compare = u"\u591a\U00005b57\x82\x88码"
```

To process an UTF-8 string on the code point level, convert the `std::string` into `std::u32string` (throws `range_error` on failure).

```cpp
    std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t> cv;
    std::u32string utf32Str = cv.from_bytes(utf8Str)
    // Do some processing here
    // std::iscntrl not only works for char, but also char16_t and char32_t
    std::string result = cv.to_bytes(utf32Str)
```

You don't need to do the conversion if you only care about the ASCII characters in the string, because UTF-8 has excellent compatibility with ASCII.

```cpp
    for (const char& ch: utf8Str)
    {
        if (ch >= 0)
        {
            // ch is ASCII
        }
    }
```

If you want finer control over the UTF-8 string, you need to use 3rd party libraries like UTF8-CPP or ICU, which adds to your binary size.

### Python 2
```python
    u = u"\u591a\U00005b57节码"
    u += unichr(40960)

    str8 = u.encode('utf-8')
    str16 = u.encode('utf-16')
    str32 = u.encode('utf-32')
```

Python may represents Unicode strings as either 16- or 32-bit integers internally, so always use Unicode string literals with prefix "u".

```python
    u = unicode(u"字符串常量")
```

All `basestring` interfaces work on code point level instead of byte level for `unicode` objects.

```python
    len(u) == 5
    u[-1] == u"量"
    u.find(u"串") == 2
```

### Python 3
```python
    s = "\u591a\U00005b57节码"
    s += chr(40960)

    bytes8 = u.encode('utf-8')
    bytes16 = u.encode('utf-16')
    bytes32 = u.encode('utf-32')
```

Since Python 3.0, the language's `str` type contains Unicode characters. Encodings coverts to `bytes` objects.

All string interfaces work on code point level.

	
	
## Q & A?

- When we do `copy and paste`? What do we copy exactly?
- Why does UTF-16 & UTF-32 not support The **Boyer-Moore** fast search algorithm?
- When do we not to use UTF-8？
	- no need to communicate internationally and save space 
	
## Thanks

- [UTF-8 and Unicode](http://www.utf-8.com/)
- [Introduction to Unicode and UTF-8](https://flaviocopes.com/unicode/#scripts)	
- [@davidxk](https://github.com/davidxk)