"""
서비스 종류에 따라 알맞은 내용을 포함하는 프로필을 생성하는 프로그램
"""

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal")


class AlbumSection(Section):
    def describe(self):
        print("Album")


class PatentSection(Section):
    def describe(self):
        print("Patent")


class PublicationSection(Section):
    def describe(self):
        print("Publication")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("which profile you'd like to create LinkedIn for Facebook")
    profile = eval(profile_type.lower())()
    print("create profile", type(profile).__name__)
    print("Profile has sections -- ", profile.getSections())

