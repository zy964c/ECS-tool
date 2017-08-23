import win32com.client

catia = win32com.client.Dispatch('catia.application')
productDocument1 = catia.ActiveDocument
Product = productDocument1.Product
collection = Product.Products
documents = catia.Documents

for i in xrange(1, collection.Count+1):
    child_prod = collection.Item(i)
    pn = child_prod.PartNumber[6:]
    pn_for_carm = child_prod.PartNumber[2:]
    inst_id = child_prod.Name
    if '.1' in inst_id:
        collection.Item(i).Name = inst_id.replace('.1', '')
        print inst_id
    print 'part number: ' + pn
    collection_child = child_prod.ReferenceProduct.Products
    for j in xrange(1, collection_child.Count+1):
        child_inst_id = collection_child.Item(j).Name
        if pn in child_inst_id:
            continue
        elif 'CARM' in child_inst_id:
            carm_pn = 'CA' + pn_for_carm
            collection_child.Item(j).PartNumber = carm_pn
            carm_doc = documents.Item(carm_pn + ".CATPart")
            carm_part = carm_doc.Part
            bodies = carm_part.Bodies
            part_body = bodies.Item(1)
            part_body.name = carm_pn
            hyb_bodies = carm_part.HybridBodies
            st_notes = hyb_bodies.Item('Standard Notes:')
            carm_part.InWorkObject = st_notes
            continue
        child_inst_id = 'IR' + pn + '_' + child_inst_id.replace('.1', '')
        print child_inst_id
        collection_child.Item(j).Name = child_inst_id
        
