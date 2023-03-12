print("你好，我是杜鑫源。欢迎使用我的作品，反馈通过196639982@qq.com发送，谢谢。")
a=input("输入鸡兔同笼版本问题:")
if a=="普通版本":
    print("加载中。。。")
    b=input("输入一个自己喜欢的解决办法:")
    if b=="画图法":
        c=int(input("输入头有几个："))
        d=int(input("输入脚有几只："))
        e=c*2
        f=d-e
        g=f//2
        h=c-g
        print("答案:有"+str(g)+"只鸡，有"+str(h)+"只兔。")
        print("算式："+str(c)+"×2="+str(e)+"(只)")
        print("算式："+str(d)+"-"+str(e)+"="+str(f)+"(只)")
        print("算式："+str(f)+"÷2="+str(g)+"(头)")
        print("算式："+str(c)+"-"+str(g)+"="+str(h)+"(头)")
        print("思路：画出"+str(c)+"头鸡，可以得出少"+str(f)+"只脚，选出其中的"+str(g)+"补上其脚两只。所以得出，兔有"+str(h)+"只，鸡有"+str(g)+"只。")
    elif b=="假设法":
        o=int(input("输入头有几个："))
        p=int(input("输入脚有几只："))
        q=o*2
        r=p-q
        s=r//2
        t=o-s
        print("答案：有"+str(s)+"只鸡，有"+str(h)+"只兔。")
        print("算式："+str(o)+"×2="+str(q)+"(只)")
        print("算式："+str(p)+"-"+str(q)+"="+str(r)+"(只)")
        print("算式："+str(r)+"÷2="+str(s)+"(头)")
        print("算式："+str(o)+"-"+str(s)+"="+str(h)+"(头)")
        print("思路：假如这"+str(o)+"个头变为"+str(o)+"头鸡，可以得出少"+str(r)+"只脚，因为用一头兔换一头鸡可以多出2只脚，所以选出其中的"+str(s)+"补上其脚两只。所以得出，兔有"+str(s)+"只，鸡有"+str(t)+"只。")
    else:
        print("暂未开发。。。")
elif a=="倍数版本":
    print("加载中。。。")
    i=input("知道鸡还是兔的倍数:")
    if i=="鸡":
        j=int(input("输入鸡是兔的几倍："))
        k=int(input("输入一共多少只脚："))
        l=j*2+1*4
        m=k//l
        n=m*1
        u=n*j
        print("答案：有"+str(n)+"只兔，有"+str(u)+"只鸡。")
        print("算式："+str(j)+"×2+1×4="+str(l)+"(只)")
        print("算式："+str(k)+"÷"+str(l)+"="+str(m)+"(组)")
        print("算式："+str(m)+"×1="+str(n)+"(只)")
        print("算式："+str(n)+"×"+str(j)+"="+str(u)+"(只)")
        print("思路：如果有1只兔，那么就要有"+str(j)+"只鸡，所以一共有"+str(l)+"只脚，那么就有"+str(m)+"组，因为一组里有1只兔，所以就有"+str(m)+"只兔，因为知道了有"+str(m)+"只兔，所以鸡有"+str(u)+"只。")
    elif i=="兔":
        v=int(input("输入兔是鸡的几倍："))
        w=int(input("输入一共多少只脚："))
        x=v*4+1*2
        y=w//x
        z=y*1
        a1=z*v
        print("答案：有"+str(z)+"只鸡，有"+str(a1)+"只兔。")
        print("算式："+str(v)+"×4+1×2="+str(x)+"(只)")
        print("算式："+str(w)+"÷"+str(x)+"="+str(y)+"(组)")
        print("算式："+str(y)+"×1="+str(z)+"(只)")
        print("算式："+str(z)+"×"+str(v)+"="+str(a1)+"(只)")
        print("思路：如果有1只鸡，那么就要有"+str(v)+"只兔，所以一共有"+str(x)+"只脚，那么就有"+str(y)+"组，因为一组里有1只鸡，所以就有"+str(z)+"只兔，因为知道了有"+str(z)+"只兔，所以鸡有"+str(a1)+"只。")
    else:
        print("暂未开发。。。")
else:
    print("抱歉，此程序暂不支持此版本。")