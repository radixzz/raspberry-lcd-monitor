from lib.core.cycled_list import CycledList

class ScreenDirector:

    def __init__( self ):
        self._screens = CycledList()

    def add_screen( self, screen ):
        self._screens.insert( screen )

    def next_screen( self ):
        self._screens.current().deactivate()
        self._screens.next().activate()
        print( 'Going to NextScreen' )
    
    def prev_screen( self ):
        self._screens.current().deactivate()
        self._screens.next().activate()
        print( 'Going to PrevScreen' )
    
    def get_current_screen( self ):
        return self._screens.current()

    def update( self, alcd ):
        if self._screens.current():
            self._screens.current().update( alcd )

    def release_all( self ):
        for screen in self._screens.get_list():
            screen.release()
