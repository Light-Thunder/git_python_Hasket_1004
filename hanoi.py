#!/usr/bin/env python
#2015/10/02
#-*- coding: utf-8 -*-

def hanoi(n,x,y,z):
	if n==1:
		print (x,'--->',z)
	else:
		hanoi(n-1,x,z,y)
		hanoi(1,x,y,z)
		hanoi(n-1,y,x,z)
n=int(input("please enter n:"))
hanoi(n,'x','y','z')
