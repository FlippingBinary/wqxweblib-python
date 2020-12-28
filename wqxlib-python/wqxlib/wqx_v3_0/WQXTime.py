from yattag import Doc, indent
from .SimpleContent import (
  Time,
  TimeZoneCode
)
from ..common import WQXException

class WQXTime:
  """Custom WQX datatype that defines a local time and corresponding time zone in which the time is measured."""

  __time: Time
  __timeZoneCode: TimeZoneCode

  def __init__(self):
    self.__time = None
    self.__timeZoneCode = None

  @property
  def time(self) -> Time:
    return self.__time
  @time.setter
  def time(self, val:Time) -> None:
    self.__time = Time(val)

  @property
  def timeZoneCode(self) -> TimeZoneCode:
    return self.__timeZoneCode
  @timeZoneCode.setter
  def timeZoneCode(self, val:TimeZoneCode) -> None:
    self.__timeZoneCode = TimeZoneCode(val)

  def generateXML(self):
    if self.__time is None:
      raise WQXException("Attribute 'time' is required.")
    if self.__timeZoneCode is None:
      raise WQXException("Attribute 'timeZoneCode' is required.")

    doc, tag, text, line = Doc().ttl()

    line('Time', self.__time)
    line('TimeZoneCode', self.__timeZoneCode)

    return doc.getvalue()
