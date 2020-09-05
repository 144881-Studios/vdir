class DirError(Exception) :
    pass
class FileAlreadyExistError(Exception) :
    pass
class vdir(object) :
    def __init__(self,obj) :
        self.obj = obj
        if type(self.obj) == dict :
            pass
        else :
            raise IOError
    def adddir(self,name,place="\\") :
        placen = str.split(place,"\\")
        if placen[-1] == "" :
            placen = placen[1:-1]
        else :
            placen = placen[1:-1] + [placen[-1]]
        predir = self.obj
        placedir = []
        for i in placen :
            placedir += [predir]
            try :
                predir[i]
            except KeyError :
                raise DirError("Directory not found: "+place)
            else :
                predir = predir[i]
        try :
            predir[name]
        except KeyError :
            predir[name] = {}
        else :
            raise FileAlreadyHaveError
        try :
            placedir[-1]
        except IndexError :
            self.obj[name] = {}
            return self
        else :
            placedir[-1] = predir
            for i in range(-1,-len(placedir),-1) :
                placedir[i-1][placen[i]] = placedir[i]
            return vdir(placedir[0])
    def addfile(self,name,place="\\") :
        placen = str.split(place,"\\")
        if placen[-1] == "" :
            placen = placen[1:-1]
        else :
            placen = placen[1:-1] + [placen[-1]]
        predir = self.obj
        placedir = []
        for i in placen :
            placedir += [predir]
            try :
                predir[i]
            except KeyError :
                raise DirError("Directory not found: "+place)
            else :
                predir = predir[i]
        try :
            predir[name]
        except KeyError :
            predir[name] = ""
        else :
            raise FileAlreadyHaveError
        try :
            placedir[-1]
        except IndexError :
            self.obj[name] = ""
            return self
        else :
            placedir[-1] = predir
            for i in range(-1,-len(placedir),-1) :
                placedir[i-1][placen[i]] = placedir[i]
            return vdir(placedir[0])
