    while True:
                parent = current
                if value < current.value:
                    # current is updated with current.left to check if left slot is empty
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                
                # avoid duplicate so no equal value
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return