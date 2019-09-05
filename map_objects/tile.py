class Tile:
    """
    map tile properties like opacity and movement block
    """
    def __init__(self,blocked, block_sight=None):
        self.blocked = blocked
        
        #default movement blocking causes sight blocking
        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight