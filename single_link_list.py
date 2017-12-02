# coding:utf-8

class LinkIndexError(Exception):
    def __init__(self, err="linked list out of range"):
        Exception.init(self, err)

class SingleNode(object):
    "单向链表的结点"
    def __init__(self, item):
        "item 存放数据元素"
        self.item = item
        # next指向下一个节点
        self.next = None

class SingleLinkList(object):
    "单向链表"
    def __init__(self):
        self.__head = None

    def is_empty(self):
        "判断是否为空"
        return self.__head == None

    def __len__(self):
        "长度"
        # 尝试使用__len__
        # 游标指向头结点
        cur = self.__head
        count = 0
        # 遍历单链表
        while not cur is None:
            count += 1
            cur = cur.next
        return count

    def __repr__(self):
        "打印链表"
        cur = self.__head
        s = "("
        while not cur.next is None:
            s += (str(cur.item) + ", ")
            cur = cur.next
        s += str(cur.item)
        s += ")"
        return s
    def add(self, item):
        "链表头部添加元素"
        node = SingleNode(item)
        # 新元素的下一个节点指向之前的head
        node.next = self.__head
        # 添加的节点作为新的链表头
        self.__head = node
    def insert(self, pos, item):
        "指定位置添加位置"
        pass
    def append(self, item):
        "链表尾部添加元素"
        node = SingleNode(item)
        # 建立游标
        cur = self.__head
        # 遍历单链表
        while not cur.next is None:
            cur = cur.next
        cur.next = node

    def __getitem__(self, key):
        "类列表索引"
        # 切片以后再写
        # if isinstance(key, int)  
        cur = self.__head
        try:
            for temp in range(key):
                cur = cur.next
            return cur.item
        except:
            raise LinkIndexError  # as e:
            # print(e)

    def insert(self, pos, item):
        "指定位置添加元素"
        pass

    def remove(self, item):
        "删除节点"
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:
                if pre is None:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            pre = cur
            cur = cur.next


if __name__ == "__main__":
    link_list = SingleLinkList()
    link_list.add(2)
    link_list.add(3)
    link_list.add(4)
    print(link_list)
    print(len(link_list))
    print(link_list[2])
