# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
      
  
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
      
  
    # returns the number of pages
    def page_count(self):
        return (self.item_count()//self.items_per_page) +1 if self.items_per_page else 0
        
        
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if page_index > self.page_count()-1 or page_index < 0 or self.item_count() <= 0:
            return -1
        elif page_index == self.page_count()-1:
            return self.item_count() - (self.items_per_page*page_index)

        last_items = self.items_per_page*(page_index-1)
        return (self.items_per_page*(page_index+1)) - 0 if last_items < 0 else last_items
        
    
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index > self.item_count() or item_index <= 0 or self.items_per_page <= 0:
            return -1
        return item_index//self.items_per_page

if __name__ == "__main__":
    helper = PaginationHelper(['a','b','c','d','e','f'], 4)
    print(helper.page_count()) # should == 2
    print(helper.item_count()) # should == 6
    print(helper.page_item_count(0))  # should == 4
    print(helper.page_item_count(1)) # last page - should == 2
    print(helper.page_item_count(2)) # should == -1 since the page is invalid

    # page_index takes an item index and returns the page that it belongs on
    print(helper.page_index(5)) # should == 1 (zero based index)
    print(helper.page_index(2)) # should == 0
    print(helper.page_index(20)) # should == -1
    print(helper.page_index(-10)) # should == -1 because negative indexes are invalid

    print('--------')
    collection = range(1,25)
    helper2 = PaginationHelper(collection, 10)
    print(helper2.page_count()) # should == 3
    print(helper2.page_index(23)) # should == 2
    print(helper2.item_count()) # should == 24
    print(helper2.page_item_count(-10)) # should == 10

    print('--------')
    helper3 = PaginationHelper([], 10)
    print(helper3.page_index(0)) # should == -1
    print(helper3.page_index(100)) # should == -1
    print(helper3.page_item_count(0)) # should == -1

    print('--------')
    helper4 = PaginationHelper(['a'], 0)
    print(helper4.page_index(1)) # should == -1
    print(helper4.page_item_count(0)) # should == -1

    print('--------')
    helper4 = PaginationHelper(['a'], -10)
    print(helper4.page_index(0)) # should == -1
    print(helper4.page_item_count(0)) # should == -1
        
  