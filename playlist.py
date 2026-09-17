"""
Homework 2: The Playlist Shuffler -- starter.

Complete CircularPlaylist below. See HW2_The_Playlist_Shuffler.md,
Part B, for the full requirements.
"""

from typing import List, Optional


class _SongNode:
    __slots__ = ("name", "next")

    def __init__(self, name: str) -> None:
        self.name = name
        self.next: Optional["_SongNode"] = None


class CircularPlaylist:
    def __init__(self) -> None:
        self._current: Optional[_SongNode] = None  # the "currently playing" node
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def add_song(self, name: str) -> None:
        """Insert `name` at the end of the circle (its next wraps back to the head)."""
        # DONE TODO
        newsong = _SongNode(name)

        if self._current is None:
            newsong.next = newsong
            self._current = newsong
        else:
            last = self._current

            while last.next != self._current:
                last = last.next

            last.next = newsong
            newsong.next = self._current

        self._size += 1

    def skip_next(self) -> str:
        """Advance the currently-playing pointer to the next song and return its name."""
        # DONE TODO
        if self._current is None:
            raise IndexError("index out of bounds")

        self._current = self._current.next
        return self._current.name

    def remove_current(self) -> str:
        """
        Remove the currently-playing song, rewire the circle around it,
        advance to the next song, and return the name of the removed song.
        """
        # DONE TODO
        if self._current is None:
            raise IndexError("index out of bounds")

        remsong = self._current.name

        if self._size == 1:
            self._current = None
            self._size = 0
            return remsong

        previous = self._current

        while previous.next != self._current:
            previous = previous.next

        previous.next = self._current.next
        self._current = self._current.next

        self._size -= 1

        return remsong

    def elimination_shuffle(self, k: int) -> List[str]:
        """
        Repeatedly skip k-1 songs and remove the k-th (the Josephus
        pattern from Part A, Question 3), until one song remains.
        Return the removed songs in removal order, with the survivor
        as the final element of the list.
        """
        # DONE TODO
        if k <= 0:
            raise ValueError("k needs to be greater than 0")

        result = []

        while self._size > 1:
            for i in range(k - 1):
                self.skip_next()

            result.append(self.remove_current())

        if self._current is not None:
            result.append(self._current.name)

        return result