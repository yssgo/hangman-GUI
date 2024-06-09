레이아웃 관리: pack 메서드
==========================

- TOC 
    - [위젯](#widget)
    - [꾸러미](#parcel)
    - [side](#side)
        - [side='top'](#side='top')
        - [side='bottom'](#side='bottom')
        - [side='left'](#side='left')
        - [side='right'](#side='right')
    - [expand](#expand)
        - [expand=True](#expand-True)
        - [expand=False](#expand-False)
    - [anchor](#anchor)
        - [anchor='center'](#anchor-center)
        - [anchor='n' (anchor=tkinter.NORTH)](#anchor-NORTH)
        - [anchor='e' (anchor=tkinter.EAST)](#anchor-EAST)
        - [anchor='s' (anchor=tkinter.SOUTH)](#anchor-SOUTH)
        - [anchor='w' (anchor=tkinter.WEST)](#anchor-WEST)
        - [anchor='ne' (anchor=tkinter.NORTHEAST)](#anchor-NORTHEAST)
        - [anchor='se' (anchor=tkinter.SOUTHEAST)](#anchor-SOUTHEAST)
        - [anchor='sw' (anchor=tkinter.SOUTHWEST)](#anchor-SOUTHWEST)
        - [anchor='nw' (anchor=tkinter.NORTHWEST)](#anchor-NORTHWEST)
    - [fill](#fill)
        - [fill='x'](#fill-X)
        - [fill='y'](#fill-Y)
        - [fill='both'](#fill-BOTH')


- **참고**

    1. https://blog.naver.com/PostView.naver?blogId=dudwo567890&logNo=130167237607 (블로그 글, 한글)
    2. https://tcl.tk/man/tcl/TkCmd/pack.htm#M27 (Tk/Tcl 매뉴얼, 영문)


<style> code {font-family: D2Coding; }</style>

## 위젯<a id="widget"></a>

- 위젯 ( padx, pady, ipadx, ipady 의 기본값은 0)


        +--------------------------------------+
                         pady
        .      +------------------------+      .
               |        ipady           |
        .      |       + + + + +        |      .
          padx | ipadx + 내용  + ipdadx | padx
        .      |       + + + + +        |      .
               |         ipady          |
        .      +------------------------+      .
                         pady
        +--------------------------------------+

## 꾸러미<a id="parcel"></a>

- 꾸러미 ( side='top 또는 side='bottom' 일 때 )

        +--------------+-----------------------------+----------------+
        | 왼쪽 빈 공간 |             위젯            | 오른쪽 빈 공간 |
        +--------------+-----------------------------+----------------+


- 꾸러미 ( side='left 또는 side='right' 일 때)

        +-----------+
        |   위쪽    |
        |  빈 공간  |
        |           |
        +  - - - -  +
        |           |
        |    위     |
        |           |
        |    젯     |
        |           |
        +  - - - -  +
        |           |
        |  아래쪽   |
        | 빈 공간   |
        +-----------+

## side<a id="side"></a>

### side='top'<a id="side='top'"></a>

        +----------------------------+
        |     첫 번째 꾸러미         |
        +----------------------------+
        |     두 번째 꾸러미         |
        +----------------------------+
        |                            |
        |                            |
        |       남은 빈 공간         |
        |                            |
        +----------------------------+

### side='bottom'<a id="side='bottom'"></a>

        +----------------------------+
        |                            |
        |        남은 빈 공간        |
        |                            |
        |                            |
        +----------------------------+
        |     두 번째 꾸러미         |
        +----------------------------+
        |     첫 번째 꾸러미         |
        +----------------------------+

### side='left'<a id="side='left'"></a>

        +----+----+------------------+
        | 첫 | 두 |                  |
        |    |    |                  |
        | 번 | 번 |                  |
        | 째 | 째 |  빈 공간         |
        |    |    |                  |
        | 꾸 | 꾸 |                  |
        | 러 | 러 |                  |
        | 미 | 미 |                  |
        +----+----+------------------+


### side='right'<a id="side='right'"></a>

        +------------------+----+----+
        |                  | 두 | 첫 |
        |                  |    |    |
        |                  | 번 | 번 |
        |  빈 공간         | 째 | 째 |
        |                  |    |    |
        |                  | 꾸 | 꾸 |
        |                  | 러 | 러 |
        |                  | 미 | 미 |
        +------------------+----+----+

## expand<a id="expand"></a>

### expand=True<a id="expand-True"></a>

- 두 번째 위젯이  expand=True 일 때

    - side = 'top'

            +----------------------------+
            |     첫 번째 꾸러미         |
            +----------------------------+
            |                            |
            |                            |
            |     두 번째 꾸러미         |
            |                            |
            |                            |
            +----------------------------+

    - side = 'left'

            +----+-----------------------+
            | 첫 |          두           |
            |    |                       |
            | 번 |          번           |
            | 째 |          째           |
            |    |                       |
            | 꾸 |          꾸           |
            | 러 |          러           |
            | 미 |          미           |
            +----+-----------------------+

### expand=False<a id="expand-False"></a>

- 두 번째 위젯이  expand=False 일 때

    - side = 'top'

            +----------------------------+
            |     첫 번째 꾸러미         |
            +----------------------------+
            |     두 번째 꾸러미         |
            +----------------------------+
            |                            |
            |                            |
            |        빈 공간             |
            |                            |
            +----------------------------+

    - side = 'left'

            +----+----+------------------+
            | 첫 | 두 |                  |
            |    |    |                  |
            | 번 | 번 |                  |
            | 째 | 째 |      빈 공간     |
            |    |    |                  |
            | 꾸 | 꾸 |                  |
            | 러 | 러 |                  |
            | 미 | 미 |                  |
            +----+----+------------------+


## anchor<a id="anchor"></a>

### anchor='center' (anchor=tkinter.CENTER)<a id="anchor-CENTER"></a>

        +--------------------------------------+  꾸러미
        |                                      |
        |              +--------+              |
        |              |'center'|              |
        |              +--------+              |
        |                                      |
        +--------------------------------------+

### anchor='n' (anchor=tkinter.NORTH)<a id="anchor-NORTH"></a>

        +--------------+--------+--------------+  꾸러미
        |              |   'n'  |              |
        |              +--------+              |
        |                                      |
        |                                      |
        |                                      |
        +--------------------------------------+

### anchor='e' (anchor=tkinter.EAST)<a id="anchor-EAST"></a>

        +--------------------------------------+  꾸러미
        |                                      |
        |                             +--------+
        |                             |  'e'   |
        |                             +--------+
        |                                      |
        +--------------------------------------+

### anchor='s' (anchor=tkinter.SOUTH)<a id="anchor-SOUTH"></a>

        +--------------------------------------+  꾸러미
        |                                      |
        |                                      |
        |                                      |
        |              +--------+              |
        |              |   's'  |              |
        +--------------+--------+--------------+

### anchor='w' (anchor=tkinter.WEST)<a id="anchor-WEST"></a>

        +--------------------------------------+  꾸러미
        |                                      |
        +--------+                             |
        |  'w'   |                             |
        +--------+                             |
        |                                      |
        +--------------------------------------+

### anchor='ne' (anchor=tkinter.NORTHEAST)<a id="anchor-NORTHEAST"></a>

        +-----------------------------+--------+  꾸러미
        |                             | 'ne'   |
        |                             +--------+
        |                                      |
        |                                      |
        |                                      |
        +--------------------------------------+

### anchor='se' (anchor=tkinter.SOUTEAST)<a id="anchor-SOUTEAST"></a>

        +--------------------------------------+  꾸러미
        |                                      |
        |                                      |
        |                                      |
        |                             +--------+
        |                             |  'se'  |
        +-----------------------------+--------+

### anchor='sw' (anchor=tkinter.SOUTWEST)<a id="anchor-SOUTWEST"></a>

        +--------------------------------------+  꾸러미
        |                                      |
        |                                      |
        |                                      |
        +--------+                             |
        |  'sw'  |                             |
        +--------+-----------------------------+

### anchor='nw' (anchor=tkinter.NORTHWEST)<a id="anchor-NORTHWEST"></a>

        +--------------------------------------+  꾸러미
        |  'nw'  |                             |
        +--------+                             |
        |                                      |
        |                                      |
        |                                      |
        +--------------------------------------+

## fill<a id="fill"></a>

### fill='x'<a id="fill-X"></a>

        | p   i  + + + + + + + + + + + + + + + + + + +  i   p |
        | a   p  +                .    .             +  p   a |
        | d | a  +                .내용.             +  a | d |
        | x   d  +                .    .             +  d   x |
        |     x  + + + + + + + + + + + + + + + + + + +  x     |


### fill='y'<a id="fill-Y"></a>

         -------
          pady
          - - -
          ipady
        + + + + +
        +       +
        +       +
        +       +
        + . . . +
        + 내용  +
        + . . . +
        +       +
        +       +
        +       +
        +       +
        + + +  +
          ipady
          - - -
          pady
         -------

### fill='both'<a id="fill-BOTH'"></a>

                                     -------
                                      pady
                                      - - -
                                      ipady
        |        + + + + + + + + + + + + + + + + + + + + +        |
        |        +                                       +        |
        | p   i  +                                       +  i   p |
        | a   p  +                  . . . .              +  p   a |
        | d | a  +                  .내용 .              +  a | d |
        | x   d  +                  . . . .              +  d   x |
        |     x  +                                       +  x     |
        |        +                                       +        |
        |        + + + + + + + + + + + + + + + + + + + + +        |
                                      ipady
                                      - - -
                                      pady
                                     -------
