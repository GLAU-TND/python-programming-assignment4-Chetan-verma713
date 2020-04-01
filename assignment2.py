def fun(nesteddict,dic,currentkey):
    for key in nesteddict.keys():
        if type(nesteddict[key]) == int:
            dic[(currentkey + "." + key).strip(".")]
        else:
            dic = fun(nesteddict[key],dic,(currentkey + "." + key).strip("."))
    return dic
def fun_dic(nesteddict):
    return(nesteddict,dict(),"")
def main():
    nesteddict = {
        "key":3,
        "foo":{
            "a":5,
            "bar":{
                "baz":8
            }
        }
    }
    dicten = fun_dic(nesteddict)
    print(dicten)
if __name__=="__main__":
    main()
