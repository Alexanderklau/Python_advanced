# coding: utf-8
__author__ = 'lau.wenbo'




def generate_fsid(self, sourceip):
    rpcclient = rpc.RpcClient()
    while True:
        fsid = random.randint(100, 900)
        check_message = "grep \"fsid=%s\" %s" % (fsid, self.nfs_conf)
        (status, output) = rpcclient.send_message(sourceip, "exe", check_message, "", 5)
        # 检查fsid，如果存在就继续生成，直到不存在为止。
        if len(output) > 9:
            pass
        else:
            return fsid

def generate_cidr_ips(self, ip, cidr):
    rpcclient = rpc.RpcClient()
    ip_cidr = "%s/%s" % (ip, cidr)
    if int(cidr) > 20:
        ip = IPNetwork(ip_cidr)
    ip_list = list(ip)



def add_nfs_list(self, id, ip, cidr, privilege):
    ret = {}
    ret["code"] = 200
    name = id
    name = name.strip('\n')
    obj = sysdb.Sysdb(self.database)
    # if obj.is_exist(id):
    #       return (-1, "subspacename existed")
    value = obj.get(id)
    if value[0] != 0:
        return (-1, "Get subspace info failed : %s" % value[1])
    space = eval(value[1])
    sourceip = space["ip"]
    rpcclient = rpc.RpcClient()

    ip_cidr = "%s/%s" % (ip, cidr)
    path = "/%s/%s" % (self.fs_name, id)
    fsid = generate_fsid(sl)

    # if len(ip_list) > 20:
    #     b = ip.split(".")[0]
    #     c = ip.split(".")[1]
    #     d = ip.split(".")[2]
    #     ips = [b + "." + c + "." + d + ".*"]
    #     if privilege == 1:
    #         fsid = generate_fsid(self, sourceip=sourceip)
    #         message = "echo \"%s        %s(rw,no_root_squash,async,fsid=%s)\" >> %s" % (path, ips, fsid, self.nfs_conf)
    #     elif privilege == 0:
    #         message = "sed -i \'/%s/d\' > %s" % (ips, self.nfs_conf)
    #     else:
    #         return (-1, "Error code!")
    #     (status, output) = rpcclient.send_message(sourceip, "exe", message, "", 5)
    #     if status != 0:
    #         return (-1, output)
    #
    # else:
    #     for i in ip_list:
    #         if privilege == 1:
    #             fsid = generate_fsid(self, sourceip = sourceip)
    #             message = "echo \"%s        %s(rw,no_root_squash,async,fsid=%s)\" >> %s" % \
    #                       (path, i, fsid, self.nfs_conf)
    #             (status, output) = rpcclient.send_message(sourceip, "exe", message, "", 5)
    #             if status != 0:
    #                 return (-1, output)
    #         elif privilege == 0:
    #             print i
    #             message = "sed -i \'/%s/d\' %s" % (i, self.nfs_conf)
    #             (status, output) = rpcclient.send_message(sourceip, "exe", message, "", 5)
    #             if status != 0:
    #                 return (-1, output)
    #         else:
    #             return (-1, "Error code!")
