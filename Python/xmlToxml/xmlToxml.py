#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
import xml.sax
import sys

# 记录slot信息
class Slot:
    def __init__(self):
        self.Number = ""
        self.Config = ""
        self.UseFlag = ""
        self.UpdateCount = ""
        self.Mode = ""
        self.HostTargetKey = ""
        self.SnPad = ""
        self.Data = ""

    def showInfo(self):
        print("    Number", self.Number)
        print("    Config", self.Config)
        print("    UseFlag", self.UseFlag)
        print("    UpdateCount", self.UpdateCount)
        print("    Mode", self.Mode)
        print("    HostTargetKey", self.HostTargetKey)
        print("    SnPad", self.SnPad)
        print("    Data", self.Data)

# 记录Opt信息
class Opt:
    def __init__(self):
        self.Mode = ""
        self.OTP_Mode = ""
        self.Data = ""

    def showInfo(self):
        print("    Mode", self.Mode)
        print("    OTP_Mode", self.OTP_Mode)
        print("    Data", self.Data)

# 记录配置信息
class Configuration:
    def __init__(self):
        self.TWI_Address = ""
        self.Temp_Offset = ""
        self.SelectorMode = ""
        self.UserExtra = ""
        self.Selector = ""

    def showInfo(self):
        print("    TWI_Address", self.TWI_Address)
        print("    Temp_Offset", self.Temp_Offset)
        print("    SelectorMode", self.SelectorMode)
        print("    UserExtra", self.UserExtra)
        print("    Selector", self.Selector)

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.index = 0
        self.slotnum = -1
        self.configFlag = 0
        self.slotFlag = 0
        self.optFlag = 0
        self.CurrentData = ""
        self.Version = ""
        self.PartNumber = ""
        self.Comm_Method = ""
        self.Session_Key_Slot = ""
        self.LastKeyUse = ""
        self.slot = [Slot() for i in range(16)]
        self.config = Configuration()
        self.opt = Opt()

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        self.index = self.index + 1

        # 标记接下来解析的是configuration
        if tag == "Configuration":
            self.configFlag =  1
            print('正在解析config')

        # 标记接下来解析的是opt
        if tag == "OTP":
            self.optFlag =  1
            print('正在解析opt')

        # 标记记下来解析的是slot
        if tag == "Slot":
            self.slotnum =  self.slotnum + 1
            self.slotFlag =  1
            print('正在解析Slot， slotnum:', self.slotnum)

        for index in range(self.index):
            print('    ', end="")
        print(self.CurrentData, end=" : ")


    # 元素结束事件处理
    def endElement(self, tag):
        # 取消标记接下来解析的是configuration
        if tag == "Configuration":
            self.configFlag =  0
            print('完成config解析')

        # 取消标记接下来解析的是opt
        if tag == "OTP":
            self.optFlag =  0
            print('完成opt解析')

        # 取消标记记下来解析的是slot
        if tag == "Slot":
            self.slotFlag =  0
            print('完成slot解析')

        self.CurrentData = ""
        self.index = self.index - 1
 
    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "Version":
            self.Version = content
        elif self.CurrentData == "PartNumber":
            self.PartNumber = content
        elif self.CurrentData == "Comm_Method":
            self.Comm_Method = content
        elif self.CurrentData == "Session_Key_Slot":
            self.Session_Key_Slot = content
        elif self.CurrentData == "LastKeyUse":
            self.LastKeyUse = content
        elif self.configFlag == 1:
            if self.CurrentData == "TWI_Address":
                self.config.TWI_Address = content
            elif self.CurrentData == "Temp_Offset":
                self.config.Temp_Offset = content
            elif self.CurrentData == "SelectorMode":
                self.config.SelectorMode = content
            elif self.CurrentData == "UserExtra":
                self.config.UserExtra = content
            elif self.CurrentData == "Selector":
                self.config.Selector = content
        elif self.optFlag == 1:
            if self.CurrentData == "Mode":
                self.opt.Mode = content
            elif self.CurrentData == "OTP_Mode":
                self.opt.OTP_Mode = content
            elif self.CurrentData == "Data":
                self.opt.Data = content
        elif self.slotFlag == 1:
            if self.CurrentData == "Number":
                self.slot[self.slotnum].Number = content
            elif self.CurrentData == "Config":
                self.slot[self.slotnum].Config = content
            elif self.CurrentData == "UseFlag":
                self.slot[self.slotnum].UseFlag = content
            elif self.CurrentData == "UpdateCount":
                self.slot[self.slotnum].UpdateCount = content
            elif self.CurrentData == "Mode":
                self.slot[self.slotnum].Mode = content
            elif self.CurrentData == "HostTargetKey":
                self.slot[self.slotnum].HostTargetKey = content
            elif self.CurrentData == "SnPad":
                self.slot[self.slotnum].SnPad = content
            elif self.CurrentData == "Data":
                self.slot[self.slotnum].Data = content
        print(content, end="")
        
  
    def showInfo(self):
            print("Version:", self.Version)
            print("PartNumber:", self.PartNumber)
            print("Comm_Method:", self.Comm_Method)
            print("Session_Key_Slot:", self.Session_Key_Slot)
            print("LastKeyUse:", self.LastKeyUse)
            print("config:")
            self.config.showInfo()
            print("opt:")
            self.opt.showInfo()
            
            for i in range(len(self.slot)):
                print("Slot:")
                self.slot[i].showInfo()

    def writeInfoToXml(self, filename):
        with open(filename, 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<SHA204Content.01>\n')
            f.write('    <ConfigZone>\n')
            f.write('        <Version>'+self.Version+'</Version>\n')
            f.write('        <PartNumber>'+self.PartNumber+'</PartNumber>\n')
            f.write('        <Comm_Method>'+self.Comm_Method+'</Comm_Method>\n')
            f.write('        <Session_Key_Slot>'+self.Session_Key_Slot+'</Session_Key_Slot>\n')
            f.write('        <Sn0to1>01 23</Sn0to1>\n')
            f.write('        <Sn2to3>51 45</Sn2to3>\n')
            f.write('        <RevNum>80 03 03 00</RevNum>\n')
            f.write('        <Sn4to7>29 AB 21 37</Sn4to7>\n')
            f.write('        <Sn8>EE</Sn8>\n')
            f.write('        <Reserved13>55</Reserved13>\n')
            f.write('        <TWI_Enable>01</TWI_Enable>\n')
            f.write('        <Reserved15>FF</Reserved15>\n')
            f.write('        <TWI_Address>'+self.config.TWI_Address+'</TWI_Address>\n')
            f.write('        <TempOffset>'+self.config.Temp_Offset+'</TempOffset>\n')
            f.write('        <OTPmode>'+self.opt.OTP_Mode+'</OTPmode>\n')
            f.write('        <SelectorMode>'+self.config.SelectorMode+'</SelectorMode>\n')
            f.write('        <SlotConfig00>'+self.slot[0].Config+'</SlotConfig00>\n')
            f.write('        <SlotConfig01>'+self.slot[1].Config+'</SlotConfig01>\n')
            f.write('        <SlotConfig02>'+self.slot[2].Config+'</SlotConfig02>\n')
            f.write('        <SlotConfig03>'+self.slot[3].Config+'</SlotConfig03>\n')
            f.write('        <SlotConfig04>'+self.slot[4].Config+'</SlotConfig04>\n')
            f.write('        <SlotConfig05>'+self.slot[5].Config+'</SlotConfig05>\n')
            f.write('        <SlotConfig06>'+self.slot[6].Config+'</SlotConfig06>\n')
            f.write('        <SlotConfig07>'+self.slot[7].Config+'</SlotConfig07>\n')
            f.write('        <SlotConfig08>'+self.slot[8].Config+'</SlotConfig08>\n')
            f.write('        <SlotConfig09>'+self.slot[9].Config+'</SlotConfig09>\n')
            f.write('        <SlotConfig0A>'+self.slot[10].Config+'</SlotConfig0A>\n')
            f.write('        <SlotConfig0B>'+self.slot[11].Config+'</SlotConfig0B>\n')
            f.write('        <SlotConfig0C>'+self.slot[12].Config+'</SlotConfig0C>\n')
            f.write('        <SlotConfig0D>'+self.slot[13].Config+'</SlotConfig0D>\n')
            f.write('        <SlotConfig0E>'+self.slot[14].Config+'</SlotConfig0E>\n')
            f.write('        <SlotConfig0F>'+self.slot[15].Config+'</SlotConfig0F>\n')
            f.write('        <UseFlag00>'+self.slot[0].UseFlag+'</UseFlag00>\n')
            f.write('        <UpdateCount00>'+self.slot[0].UpdateCount+'</UpdateCount00>\n')
            f.write('        <UseFlag01>'+self.slot[1].UseFlag+'</UseFlag01>\n')
            f.write('        <UpdateCount01>'+self.slot[1].UpdateCount+'</UpdateCount01>\n')
            f.write('        <UseFlag02>'+self.slot[2].UseFlag+'</UseFlag02>\n')
            f.write('        <UpdateCount02>'+self.slot[2].UpdateCount+'</UpdateCount02>\n')
            f.write('        <UseFlag03>'+self.slot[3].UseFlag+'</UseFlag03>\n')
            f.write('        <UpdateCount03>'+self.slot[3].UpdateCount+'</UpdateCount03>\n')
            f.write('        <UseFlag04>'+self.slot[4].UseFlag+'</UseFlag04>\n')
            f.write('        <UpdateCount04>'+self.slot[4].UpdateCount+'</UpdateCount04>\n')
            f.write('        <UseFlag05>'+self.slot[5].UseFlag+'</UseFlag05>\n')
            f.write('        <UpdateCount05>'+self.slot[5].UpdateCount+'</UpdateCount05>\n')
            f.write('        <UseFlag06>'+self.slot[6].UseFlag+'</UseFlag06>\n')
            f.write('        <UpdateCount06>'+self.slot[6].UpdateCount+'</UpdateCount06>\n')
            f.write('        <UseFlag07>'+self.slot[7].UseFlag+'</UseFlag07>\n')
            f.write('        <UpdateCount07>'+self.slot[7].UpdateCount+'</UpdateCount07>\n')
            f.write('        <LastKeyUse>'+self.LastKeyUse+'</LastKeyUse>\n')
            f.write('        <UserExtra>'+self.config.UserExtra+'</UserExtra>\n')
            f.write('        <Selector>'+self.config.Selector+'</Selector>\n')
            f.write('        <Reserved8485>00 00</Reserved8485>\n')
            f.write('        <LockValue>55</LockValue>\n')
            f.write('        <LockConfig>00</LockConfig>\n')
            f.write('    </ConfigZone>\n')
            f.write('    <OtpZone>'+self.opt.Data+'</OtpZone>\n')
            f.write('    <DataZone>\n')
            f.write('        <Slot>'+self.slot[0].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[1].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[2].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[3].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[4].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[5].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[6].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[7].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[8].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[9].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[10].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[11].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[12].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[13].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[14].Data+'</Slot>\n')
            f.write('        <Slot>'+self.slot[15].Data+'</Slot>\n')
            f.write('\n')
            f.write('    </DataZone>\n')
            f.write('</SHA204Content.01>\n')
        print("write to file ok:"+filename)

