import win32com.client

catia = win32com.client.Dispatch('catia.application')
productDocument1 = catia.ActiveDocument
Product = productDocument1.Product
collection = Product.Products

for i in xrange(1, collection.Count+1):
    child_prod = collection.Item(i)
    pn = child_prod.PartNumber[6:]
    inst_id = child_prod.Name
    if '.1' in inst_id:
        collection.Item(i).Name = inst_id.replace('.1', '')
        print inst_id
    print 'part number: ' + pn
    collection_child = child_prod.ReferenceProduct.Products
    for j in xrange(1, collection_child.Count+1):
        child_inst_id = collection_child.Item(j).Name
        if pn in child_inst_id or 'CARM' in child_inst_id:
            continue
        child_inst_id = 'IR' + pn + '_' + child_inst_id.replace('.1', '')
        print child_inst_id
        collection_child.Item(j).Name = child_inst_id
        
