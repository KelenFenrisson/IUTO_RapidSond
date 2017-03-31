#!/usr/bin/env python
# encoding: utf-8
# Généré par Mocodo 2.3.7 le Fri, 31 Mar 2017 12:56:26

from __future__ import division
from math import hypot

import time, codecs

(width,height) = (1144,729)
cx = {
    u"VILLE"                   : 1026,
    u"FAIRE_PARTIE"            :  629,
    u"CSP"                     :  819,
    u"ETRE_DANS"               : 1026,
    u"APPARTENIR"              :  431,
    u"SONDE"                   :  629,
    u"SONDE_AVOIR_ADRESSE"     :  819,
    u"ADRESSE"                 : 1026,
    u"CHOIX_MULTIPLE"          :   86,
    u"PANEL"                   :  431,
    u"CONCERNER"               :  629,
    u"ENTREPRISE_AVOIR_ADRESSE": 1026,
    u"ASSOCIER"                :   86,
    u"QUESTION"                :  233,
    u"CONSTITUER"              :  431,
    u"QUESTIONNAIRE"           :  629,
    u"ACHETER"                 :  819,
    u"ENTREPRISE"              : 1026,
    u"AVOIR_TYPE_QUESTION"     :  233,
    u"TYPE_QUESTION"           :  431,
}
cy = {
    u"VILLE"                   :   53,
    u"FAIRE_PARTIE"            :  147,
    u"CSP"                     :  147,
    u"ETRE_DANS"               :  147,
    u"APPARTENIR"              :  286,
    u"SONDE"                   :  286,
    u"SONDE_AVOIR_ADRESSE"     :  286,
    u"ADRESSE"                 :  286,
    u"CHOIX_MULTIPLE"          :  425,
    u"PANEL"                   :  425,
    u"CONCERNER"               :  425,
    u"ENTREPRISE_AVOIR_ADRESSE":  425,
    u"ASSOCIER"                :  555,
    u"QUESTION"                :  555,
    u"CONSTITUER"              :  555,
    u"QUESTIONNAIRE"           :  555,
    u"ACHETER"                 :  555,
    u"ENTREPRISE"              :  555,
    u"AVOIR_TYPE_QUESTION"     :  685,
    u"TYPE_QUESTION"           :  685,
}
shift = {
    u"FAIRE_PARTIE,SONDE"                 :    0,
    u"FAIRE_PARTIE,CSP"                   :    0,
    u"ETRE_DANS,ADRESSE"                  :    0,
    u"ETRE_DANS,VILLE"                    :    0,
    u"APPARTENIR,PANEL"                   :    0,
    u"APPARTENIR,SONDE"                   :    0,
    u"SONDE_AVOIR_ADRESSE,SONDE"          :    0,
    u"SONDE_AVOIR_ADRESSE,ADRESSE"        :    0,
    u"CONCERNER,QUESTIONNAIRE"            :    0,
    u"CONCERNER,PANEL"                    :    0,
    u"ENTREPRISE_AVOIR_ADRESSE,ENTREPRISE":    0,
    u"ENTREPRISE_AVOIR_ADRESSE,ADRESSE"   :    0,
    u"ASSOCIER,CHOIX_MULTIPLE"            :    0,
    u"ASSOCIER,QUESTION"                  :    0,
    u"CONSTITUER,QUESTION"                :    0,
    u"CONSTITUER,QUESTIONNAIRE"           :    0,
    u"ACHETER,QUESTIONNAIRE"              :    0,
    u"ACHETER,ENTREPRISE"                 :    0,
    u"AVOIR_TYPE_QUESTION,QUESTION"       :    0,
    u"AVOIR_TYPE_QUESTION,TYPE_QUESTION"  :    0,
}
ratio = {
    u"FAIRE_PARTIE,CSP"                 :  1.00,
    u"ETRE_DANS,VILLE"                  :  1.00,
    u"CONCERNER,PANEL"                  :  1.00,
    u"ASSOCIER,QUESTION"                :  1.00,
    u"CONSTITUER,QUESTIONNAIRE"         :  1.00,
    u"ACHETER,ENTREPRISE"               :  1.00,
    u"AVOIR_TYPE_QUESTION,TYPE_QUESTION":  1.00,
}
colors = {
    u"annotation_color"                : '#060707',
    u"annotation_text_color"           : '#E2EED0',
    u"association_attribute_text_color": '#607734',
    u"association_cartouche_color"     : '#b2bba4',
    u"association_cartouche_text_color": '#27360c',
    u"association_color"               : '#ccd6ba',
    u"association_stroke_color"        : '#85956b',
    u"background_color"                : 'none',
    u"card_text_color"                 : '#726f83',
    u"entity_attribute_text_color"     : '#3e3c42',
    u"entity_cartouche_color"          : '#97b8ff',
    u"entity_cartouche_text_color"     : '#131114',
    u"entity_color"                    : '#c0d4ff',
    u"entity_stroke_color"             : '#578dff',
    u"label_text_color"                : '#726f83',
    u"leg_stroke_color"                : '#726f83',
    u"transparent_color"               : 'none',
}
card_max_width = 23
card_max_height = 14
card_margin = 5
arrow_width = 12
arrow_half_height = 6
arrow_axis = 8
card_baseline = 3

def cmp(x, y):
    return (x > y) - (x < y)

def offset(x, y):
    return (x + card_margin, y - card_baseline - card_margin)

def line_intersection(ex, ey, w, h, ax, ay):
    if ax == ex:
        return (ax, ey + cmp(ay, ey) * h)
    if ay == ey:
        return (ex + cmp(ax, ex) * w, ay)
    x = ex + cmp(ax, ex) * w
    y = ey + (ay-ey) * (x-ex) / (ax-ex)
    if abs(y-ey) > h:
        y = ey + cmp(ay, ey) * h
        x = ex + (ax-ex) * (y-ey) / (ay-ey)
    return (x, y)

def straight_leg_factory(ex, ey, ew, eh, ax, ay, aw, ah, cw, ch):
    
    def card_pos(twist, shift):
        compare = (lambda x1_y1: x1_y1[0] < x1_y1[1]) if twist else (lambda x1_y1: x1_y1[0] <= x1_y1[1])
        diagonal = hypot(ax-ex, ay-ey)
        correction = card_margin * 1.4142 * (1 - abs(abs(ax-ex) - abs(ay-ey)) / diagonal) - shift
        (xg, yg) = line_intersection(ex, ey, ew, eh + ch, ax, ay)
        (xb, yb) = line_intersection(ex, ey, ew + cw, eh, ax, ay)
        if compare((xg, xb)):
            if compare((xg, ex)):
                if compare((yb, ey)):
                    return (xb - correction, yb)
                return (xb - correction, yb + ch)
            if compare((yb, ey)):
                return (xg, yg + ch - correction)
            return (xg, yg + correction)
        if compare((xb, ex)):
            if compare((yb, ey)):
                return (xg - cw, yg + ch - correction)
            return (xg - cw, yg + correction)
        if compare((yb, ey)):
            return (xb - cw + correction, yb)
        return (xb - cw + correction, yb + ch)
    
    def arrow_pos(direction, ratio):
        (x0, y0) = line_intersection(ex, ey, ew, eh, ax, ay)
        (x1, y1) = line_intersection(ax, ay, aw, ah, ex, ey)
        if direction == "<":
            (x0, y0, x1, y1) = (x1, y1, x0, y0)
        (x, y) = (ratio * x0 + (1 - ratio) * x1, ratio * y0 + (1 - ratio) * y1)
        return (x, y, x1 - x0, y0 - y1)
    
    straight_leg_factory.card_pos = card_pos
    straight_leg_factory.arrow_pos = arrow_pos
    return straight_leg_factory


def curved_leg_factory(ex, ey, ew, eh, ax, ay, aw, ah, cw, ch, spin):
    
    def bisection(predicate):
        (a, b) = (0, 1)
        while abs(b - a) > 0.0001:
            m = (a + b) / 2
            if predicate(bezier(m)):
                a = m
            else:
                b = m
        return m
    
    def intersection(left, top, right, bottom):
       (x, y) = bezier(bisection(lambda p: left <= p[0] <= right and top <= p[1] <= bottom))
       return (int(round(x)), int(round(y)))
    
    def card_pos(shift):
        diagonal = hypot(ax-ex, ay-ey)
        correction = card_margin * 1.4142 * (1 - abs(abs(ax-ex) - abs(ay-ey)) / diagonal)
        (top, bot) = (ey - eh, ey + eh)
        (TOP, BOT) = (top - ch, bot + ch)
        (lef, rig) = (ex - ew, ex + ew)
        (LEF, RIG) = (lef - cw, rig + cw)
        (xr, yr) = intersection(LEF, TOP, RIG, BOT)
        (xg, yg) = intersection(lef, TOP, rig, BOT)
        (xb, yb) = intersection(LEF, top, RIG, bot)
        if spin > 0:
            if (yr == BOT and xr <= rig) or (xr == LEF and yr >= bot):
                return (max(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y >= bot) - correction + shift, bot + ch)
            if (xr == RIG and yr >= top) or yr == BOT:
                return (rig, min(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x >= rig) + correction + shift)
            if (yr == TOP and xr >= lef) or xr == RIG:
                return (min(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y <= top) + correction + shift - cw, TOP + ch)
            return (LEF, max(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x <= lef) - correction + shift + ch)
        if (yr == BOT and xr >= lef) or (xr == RIG and yr >= bot):
            return (min(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y >= bot) + correction + shift - cw, bot + ch)
        if xr == RIG or (yr == TOP and xr >= rig):
            return (rig, max(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x >= rig) - correction + shift + ch)
        if yr == TOP or (xr == LEF and yr <= top):
            return (max(x for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if y <= top) - correction + shift, TOP + ch)
        return (LEF, min(y for (x, y) in ((xr, yr), (xg, yg), (xb, yb)) if x <= lef) + correction + shift)
    
    def arrow_pos(direction, ratio):
        t0 = bisection(lambda p: abs(p[0] - ax) > aw or abs(p[1] - ay) > ah)
        t3 = bisection(lambda p: abs(p[0] - ex) < ew and abs(p[1] - ey) < eh)
        if direction == "<":
            (t0, t3) = (t3, t0)
        tc = t0 + (t3 - t0) * ratio
        (xc, yc) = bezier(tc)
        (x, y) = derivate(tc)
        if direction == "<":
            (x, y) = (-x, -y)
        return (xc, yc, x, -y)
    
    diagonal = hypot(ax - ex, ay - ey)
    (x, y) = line_intersection(ex, ey, ew + cw / 2, eh + ch / 2, ax, ay)
    k = (cw *  abs((ay - ey) / diagonal) + ch * abs((ax - ex) / diagonal))
    (x, y) = (x - spin * k * (ay - ey) / diagonal, y + spin * k * (ax - ex) / diagonal)
    (hx, hy) = (2 * x - (ex + ax) / 2, 2 * y - (ey + ay) / 2)
    (x1, y1) = (ex + (hx - ex) * 2 / 3, ey + (hy - ey) * 2 / 3)
    (x2, y2) = (ax + (hx - ax) * 2 / 3, ay + (hy - ay) * 2 / 3)
    (kax, kay) = (ex - 2 * hx + ax, ey - 2 * hy + ay)
    (kbx, kby) = (2 * hx - 2 * ex, 2 * hy - 2 * ey)
    bezier = lambda t: (kax*t*t + kbx*t + ex, kay*t*t + kby*t + ey)
    derivate = lambda t: (2*kax*t + kbx, 2*kay*t + kby)
    
    curved_leg_factory.points = (ex, ey, x1, y1, x2, y2, ax, ay)
    curved_leg_factory.card_pos = card_pos
    curved_leg_factory.arrow_pos = arrow_pos
    return curved_leg_factory


def upper_round_rect(x, y, w, h, r):
    return " ".join([str(x) for x in ["M", x + w - r, y, "a", r, r, 90, 0, 1, r, r, "V", y + h, "h", -w, "V", y + r, "a", r, r, 90, 0, 1, r, -r]])

def lower_round_rect(x, y, w, h, r):
    return " ".join([str(x) for x in ["M", x + w, y, "v", h - r, "a", r, r, 90, 0, 1, -r, r, "H", x + r, "a", r, r, 90, 0, 1, -r, -r, "V", y, "H", w]])

def arrow(x, y, a, b):
    c = hypot(a, b)
    (cos, sin) = (a / c, b / c)
    return " ".join([str(x) for x in [ "M", x, y, "L", x + arrow_width * cos - arrow_half_height * sin, y - arrow_half_height * cos - arrow_width * sin, "L", x + arrow_axis * cos, y - arrow_axis * sin, "L", x + arrow_width * cos + arrow_half_height * sin, y + arrow_half_height * cos - arrow_width * sin, "Z"]])

def safe_print_for_PHP(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode("utf8"))


lines = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
lines += '\n\n<svg width="%s" height="%s" view_box="0 0 %s %s"\nxmlns="http://www.w3.org/2000/svg"\nxmlns:link="http://www.w3.org/1999/xlink">' % (width,height,width,height)
lines += u'\\n\\n<desc>Généré par Mocodo 2.3.7 le %s</desc>' % time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
lines += '\n\n<rect id="frame" x="0" y="0" width="%s" height="%s" fill="%s" stroke="none" stroke-width="0"/>' % (width,height,colors['background_color'] if colors['background_color'] else "none")

lines += u"""\n\n<!-- Association ENTREPRISE_AVOIR_ADRESSE -->"""
(x,y) = (cx[u"ENTREPRISE_AVOIR_ADRESSE"],cy[u"ENTREPRISE_AVOIR_ADRESSE"])
(ex,ey) = (cx[u"ENTREPRISE"],cy[u"ENTREPRISE"])
leg=straight_leg_factory(ex,ey,73,53,x,y,109,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ENTREPRISE_AVOIR_ADRESSE,ENTREPRISE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ADRESSE"],cy[u"ADRESSE"])
leg=straight_leg_factory(ex,ey,86,89,x,y,109,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ENTREPRISE_AVOIR_ADRESSE,ADRESSE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-ENTREPRISE_AVOIR_ADRESSE">""" % {}
path = upper_round_rect(-109+x,-26+y,218,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-109+x,0.0+y,218,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="218" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -109+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -109+x, 'y0': 0+y, 'x1': 109+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">ENTREPRISE_AVOIR_ADRESSE</text>""" % {'x': -102+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association AVOIR_TYPE_QUESTION -->"""
(x,y) = (cx[u"AVOIR_TYPE_QUESTION"],cy[u"AVOIR_TYPE_QUESTION"])
(ex,ey) = (cx[u"QUESTION"],cy[u"QUESTION"])
leg=straight_leg_factory(ex,ey,73,44,x,y,88,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"AVOIR_TYPE_QUESTION,QUESTION"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"TYPE_QUESTION"],cy[u"TYPE_QUESTION"])
leg=straight_leg_factory(ex,ey,77,35,x,y,88,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"AVOIR_TYPE_QUESTION,TYPE_QUESTION"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"AVOIR_TYPE_QUESTION,TYPE_QUESTION"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-AVOIR_TYPE_QUESTION">""" % {}
path = upper_round_rect(-88+x,-26+y,176,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-88+x,0.0+y,176,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="176" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -88+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -88+x, 'y0': 0+y, 'x1': 88+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">AVOIR_TYPE_QUESTION</text>""" % {'x': -81+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association CONCERNER -->"""
(x,y) = (cx[u"CONCERNER"],cy[u"CONCERNER"])
(ex,ey) = (cx[u"QUESTIONNAIRE"],cy[u"QUESTIONNAIRE"])
leg=straight_leg_factory(ex,ey,115,71,x,y,46,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"CONCERNER,QUESTIONNAIRE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"PANEL"],cy[u"PANEL"])
leg=straight_leg_factory(ex,ey,65,35,x,y,46,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"CONCERNER,PANEL"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"CONCERNER,PANEL"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-CONCERNER">""" % {}
path = upper_round_rect(-46+x,-26+y,92,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-46+x,0.0+y,92,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="92" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -46+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -46+x, 'y0': 0+y, 'x1': 46+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">CONCERNER</text>""" % {'x': -39+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association ETRE_DANS -->"""
(x,y) = (cx[u"ETRE_DANS"],cy[u"ETRE_DANS"])
(ex,ey) = (cx[u"ADRESSE"],cy[u"ADRESSE"])
leg=straight_leg_factory(ex,ey,86,89,x,y,46,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ETRE_DANS,ADRESSE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"VILLE"],cy[u"VILLE"])
leg=straight_leg_factory(ex,ey,73,44,x,y,46,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ETRE_DANS,VILLE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"ETRE_DANS,VILLE"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-ETRE_DANS">""" % {}
path = upper_round_rect(-46+x,-26+y,92,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-46+x,0.0+y,92,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="92" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -46+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -46+x, 'y0': 0+y, 'x1': 46+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">ETRE_DANS</text>""" % {'x': -39+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association CONSTITUER -->"""
(x,y) = (cx[u"CONSTITUER"],cy[u"CONSTITUER"])
(ex,ey) = (cx[u"QUESTION"],cy[u"QUESTION"])
leg=straight_leg_factory(ex,ey,73,44,x,y,50,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"CONSTITUER,QUESTION"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"QUESTIONNAIRE"],cy[u"QUESTIONNAIRE"])
leg=straight_leg_factory(ex,ey,115,71,x,y,50,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"CONSTITUER,QUESTIONNAIRE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"CONSTITUER,QUESTIONNAIRE"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-CONSTITUER">""" % {}
path = upper_round_rect(-50+x,-26+y,100,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-50+x,0.0+y,100,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="100" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -50+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -50+x, 'y0': 0+y, 'x1': 50+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">CONSTITUER</text>""" % {'x': -43+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association APPARTENIR -->"""
(x,y) = (cx[u"APPARTENIR"],cy[u"APPARTENIR"])
(ex,ey) = (cx[u"PANEL"],cy[u"PANEL"])
leg=straight_leg_factory(ex,ey,65,35,x,y,50,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"APPARTENIR,PANEL"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"SONDE"],cy[u"SONDE"])
leg=straight_leg_factory(ex,ey,69,71,x,y,50,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"APPARTENIR,SONDE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-APPARTENIR">""" % {}
path = upper_round_rect(-50+x,-26+y,100,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-50+x,0.0+y,100,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="100" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -50+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -50+x, 'y0': 0+y, 'x1': 50+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">APPARTENIR</text>""" % {'x': -43+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association SONDE_AVOIR_ADRESSE -->"""
(x,y) = (cx[u"SONDE_AVOIR_ADRESSE"],cy[u"SONDE_AVOIR_ADRESSE"])
(ex,ey) = (cx[u"SONDE"],cy[u"SONDE"])
leg=straight_leg_factory(ex,ey,69,71,x,y,88,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"SONDE_AVOIR_ADRESSE,SONDE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ADRESSE"],cy[u"ADRESSE"])
leg=straight_leg_factory(ex,ey,86,89,x,y,88,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"SONDE_AVOIR_ADRESSE,ADRESSE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
lines += u"""\n<g id="association-SONDE_AVOIR_ADRESSE">""" % {}
path = upper_round_rect(-88+x,-26+y,176,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-88+x,0.0+y,176,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="176" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -88+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -88+x, 'y0': 0+y, 'x1': 88+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">SONDE_AVOIR_ADRESSE</text>""" % {'x': -81+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association FAIRE_PARTIE -->"""
(x,y) = (cx[u"FAIRE_PARTIE"],cy[u"FAIRE_PARTIE"])
(ex,ey) = (cx[u"SONDE"],cy[u"SONDE"])
leg=straight_leg_factory(ex,ey,69,71,x,y,58,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"FAIRE_PARTIE,SONDE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"CSP"],cy[u"CSP"])
leg=straight_leg_factory(ex,ey,52,35,x,y,58,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"FAIRE_PARTIE,CSP"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"FAIRE_PARTIE,CSP"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-FAIRE_PARTIE">""" % {}
path = upper_round_rect(-58+x,-26+y,116,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-58+x,0.0+y,116,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="116" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -58+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -58+x, 'y0': 0+y, 'x1': 58+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">FAIRE_PARTIE</text>""" % {'x': -51+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association ACHETER -->"""
(x,y) = (cx[u"ACHETER"],cy[u"ACHETER"])
(ex,ey) = (cx[u"QUESTIONNAIRE"],cy[u"QUESTIONNAIRE"])
leg=straight_leg_factory(ex,ey,115,71,x,y,37,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ACHETER,QUESTIONNAIRE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"ENTREPRISE"],cy[u"ENTREPRISE"])
leg=straight_leg_factory(ex,ey,73,53,x,y,37,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ACHETER,ENTREPRISE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"ACHETER,ENTREPRISE"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-ACHETER">""" % {}
path = upper_round_rect(-37+x,-26+y,74,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-37+x,0.0+y,74,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="74" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -37+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -37+x, 'y0': 0+y, 'x1': 37+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">ACHETER</text>""" % {'x': -30+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association ASSOCIER -->"""
(x,y) = (cx[u"ASSOCIER"],cy[u"ASSOCIER"])
(ex,ey) = (cx[u"CHOIX_MULTIPLE"],cy[u"CHOIX_MULTIPLE"])
leg=straight_leg_factory(ex,ey,77,35,x,y,41,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ASSOCIER,CHOIX_MULTIPLE"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
(ex,ey) = (cx[u"QUESTION"],cy[u"QUESTION"])
leg=straight_leg_factory(ex,ey,73,44,x,y,41,26,23+2*card_margin,14+2*card_margin)
lines += u"""\n<line x1="%(ex)s" y1="%(ey)s" x2="%(ax)s" y2="%(ay)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'ex': ex, 'ey': ey, 'ax': x, 'ay': y, 'stroke_color': colors['leg_stroke_color']}
(tx,ty)=offset(*leg.card_pos(False,shift[u"ASSOCIER,QUESTION"]))
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(text_color)s" font-family="Courier New" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'text_color': colors['card_text_color']}
path=arrow(*leg.arrow_pos(">",ratio[u"ASSOCIER,QUESTION"]))
lines += u"""\n<path d="%(path)s" fill="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'stroke_color': colors['leg_stroke_color']}
lines += u"""\n<g id="association-ASSOCIER">""" % {}
path = upper_round_rect(-41+x,-26+y,82,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_cartouche_color'], 'stroke_color': colors['association_cartouche_color']}
path = lower_round_rect(-41+x,0.0+y,82,26,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'path': path, 'color': colors['association_color'], 'stroke_color': colors['association_color']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="82" height="52" fill="%(color)s" rx="14" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -41+x, 'y': -26+y, 'color': colors['transparent_color'], 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -41+x, 'y0': 0+y, 'x1': 41+x, 'y1': 0+y, 'stroke_color': colors['association_stroke_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">ASSOCIER</text>""" % {'x': -34+x, 'y': -7.4+y, 'text_color': colors['association_cartouche_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity PANEL -->"""
(x,y) = (cx[u"PANEL"],cy[u"PANEL"])
lines += u"""\n<g id="entity-PANEL">""" % {}
lines += u"""\n	<g id="frame-PANEL">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="130" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -65+x, 'y': -35+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="130" height="44" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -65+x, 'y': -9.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="130" height="70" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -65+x, 'y': -35+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -65+x, 'y0': -9+y, 'x1': 65+x, 'y1': -9+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">PANEL</text>""" % {'x': -22+x, 'y': -16.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_panel</text>""" % {'x': -60+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -60+x, 'y0': 12.0+y, 'x1': 8+x, 'y1': 12.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">intitule_panel</text>""" % {'x': -60+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity TYPE_QUESTION -->"""
(x,y) = (cx[u"TYPE_QUESTION"],cy[u"TYPE_QUESTION"])
lines += u"""\n<g id="entity-TYPE_QUESTION">""" % {}
lines += u"""\n	<g id="frame-TYPE_QUESTION">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="154" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -77+x, 'y': -35+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="154" height="44" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -77+x, 'y': -9.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="154" height="70" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -77+x, 'y': -35+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -77+x, 'y0': -9+y, 'x1': 77+x, 'y1': -9+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">TYPE_QUESTION</text>""" % {'x': -55+x, 'y': -16.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_typequest</text>""" % {'x': -72+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -72+x, 'y0': 12.0+y, 'x1': 30+x, 'y1': 12.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">libelle_typequest</text>""" % {'x': -72+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity QUESTION -->"""
(x,y) = (cx[u"QUESTION"],cy[u"QUESTION"])
lines += u"""\n<g id="entity-QUESTION">""" % {}
lines += u"""\n	<g id="frame-QUESTION">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -73+x, 'y': -44+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="62" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -73+x, 'y': -18.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="88" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -73+x, 'y': -44+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -73+x, 'y0': -18+y, 'x1': 73+x, 'y1': -18+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">QUESTION</text>""" % {'x': -34+x, 'y': -25.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_question</text>""" % {'x': -68+x, 'y': 0.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -68+x, 'y0': 3.0+y, 'x1': 26+x, 'y1': 3.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">enonce_question</text>""" % {'x': -68+x, 'y': 18.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">urlanal_question</text>""" % {'x': -68+x, 'y': 36.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity QUESTIONNAIRE -->"""
(x,y) = (cx[u"QUESTIONNAIRE"],cy[u"QUESTIONNAIRE"])
lines += u"""\n<g id="entity-QUESTIONNAIRE">""" % {}
lines += u"""\n	<g id="frame-QUESTIONNAIRE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="230" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -115+x, 'y': -71+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="230" height="116" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -115+x, 'y': -45.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="230" height="142" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -115+x, 'y': -71+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -115+x, 'y0': -45+y, 'x1': 115+x, 'y1': -45+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">QUESTIONNAIRE</text>""" % {'x': -55+x, 'y': -52.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_questionnaire</text>""" % {'x': -110+x, 'y': -26.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -110+x, 'y0': -24.0+y, 'x1': 26+x, 'y1': -24.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">intitule_questionnaire</text>""" % {'x': -110+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">dateheurelim_questionnaire</text>""" % {'x': -110+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">accessible_questionnaire</text>""" % {'x': -110+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">termine_questionnaire</text>""" % {'x': -110+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">analyse_questionnaire</text>""" % {'x': -110+x, 'y': 63.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity CSP -->"""
(x,y) = (cx[u"CSP"],cy[u"CSP"])
lines += u"""\n<g id="entity-CSP">""" % {}
lines += u"""\n	<g id="frame-CSP">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="104" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -52+x, 'y': -35+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="104" height="44" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -52+x, 'y': -9.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="104" height="70" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -52+x, 'y': -35+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -52+x, 'y0': -9+y, 'x1': 52+x, 'y1': -9+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">CSP</text>""" % {'x': -13+x, 'y': -16.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_csp</text>""" % {'x': -47+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -47+x, 'y0': 12.0+y, 'x1': 5+x, 'y1': 12.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">libelle_csp</text>""" % {'x': -47+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity ENTREPRISE -->"""
(x,y) = (cx[u"ENTREPRISE"],cy[u"ENTREPRISE"])
lines += u"""\n<g id="entity-ENTREPRISE">""" % {}
lines += u"""\n	<g id="frame-ENTREPRISE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -73+x, 'y': -53+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="80" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -73+x, 'y': -27.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="106" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -73+x, 'y': -53+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -73+x, 'y0': -27+y, 'x1': 73+x, 'y1': -27+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">ENTREPRISE</text>""" % {'x': -43+x, 'y': -34.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_entreprise</text>""" % {'x': -68+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -68+x, 'y0': -6.0+y, 'x1': 42+x, 'y1': -6.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">nom_entreprise</text>""" % {'x': -68+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">tel_entreprise</text>""" % {'x': -68+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">email_entreprise</text>""" % {'x': -68+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity VILLE -->"""
(x,y) = (cx[u"VILLE"],cy[u"VILLE"])
lines += u"""\n<g id="entity-VILLE">""" % {}
lines += u"""\n	<g id="frame-VILLE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -73+x, 'y': -44+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="62" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -73+x, 'y': -18.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="146" height="88" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -73+x, 'y': -44+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -73+x, 'y0': -18+y, 'x1': 73+x, 'y1': -18+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">VILLE</text>""" % {'x': -22+x, 'y': -25.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">codeinsee_ville</text>""" % {'x': -68+x, 'y': 0.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -68+x, 'y0': 3.0+y, 'x1': 59+x, 'y1': 3.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">nom_ville</text>""" % {'x': -68+x, 'y': 18.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">codepostal_ville</text>""" % {'x': -68+x, 'y': 36.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity CHOIX_MULTIPLE -->"""
(x,y) = (cx[u"CHOIX_MULTIPLE"],cy[u"CHOIX_MULTIPLE"])
lines += u"""\n<g id="entity-CHOIX_MULTIPLE">""" % {}
lines += u"""\n	<g id="frame-CHOIX_MULTIPLE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="154" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -77+x, 'y': -35+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="154" height="44" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -77+x, 'y': -9.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="154" height="70" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -77+x, 'y': -35+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -77+x, 'y0': -9+y, 'x1': 77+x, 'y1': -9+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">CHOIX_MULTIPLE</text>""" % {'x': -60+x, 'y': -16.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_choixmul</text>""" % {'x': -72+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -72+x, 'y0': 12.0+y, 'x1': 22+x, 'y1': 12.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">intitule_choixmul</text>""" % {'x': -72+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity ADRESSE -->"""
(x,y) = (cx[u"ADRESSE"],cy[u"ADRESSE"])
lines += u"""\n<g id="entity-ADRESSE">""" % {}
lines += u"""\n	<g id="frame-ADRESSE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="172" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -86+x, 'y': -89+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="172" height="152" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -86+x, 'y': -63.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="172" height="178" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -86+x, 'y': -89+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -86+x, 'y0': -63+y, 'x1': 86+x, 'y1': -63+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">ADRESSE</text>""" % {'x': -30+x, 'y': -70.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_adresse</text>""" % {'x': -81+x, 'y': -44.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -81+x, 'y0': -42.0+y, 'x1': 4+x, 'y1': -42.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">numero_adresse</text>""" % {'x': -81+x, 'y': -26.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">bister_adresse</text>""" % {'x': -81+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">libellevoie_adresse</text>""" % {'x': -81+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">batiment_adresse</text>""" % {'x': -81+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">etage_adresse</text>""" % {'x': -81+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">escalier_adresse</text>""" % {'x': -81+x, 'y': 63.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">appartement_adresse</text>""" % {'x': -81+x, 'y': 81.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity SONDE -->"""
(x,y) = (cx[u"SONDE"],cy[u"SONDE"])
lines += u"""\n<g id="entity-SONDE">""" % {}
lines += u"""\n	<g id="frame-SONDE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="138" height="26" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -69+x, 'y': -71+y, 'color': colors['entity_cartouche_color'], 'stroke_color': colors['entity_cartouche_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="138" height="116" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="0"/>""" % {'x': -69+x, 'y': -45.0+y, 'color': colors['entity_color'], 'stroke_color': colors['entity_color']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="138" height="142" fill="%(color)s" stroke="%(stroke_color)s" stroke-width="1.5"/>""" % {'x': -69+x, 'y': -71+y, 'color': colors['transparent_color'], 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -69+x, 'y0': -45+y, 'x1': 69+x, 'y1': -45+y, 'stroke_color': colors['entity_stroke_color']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">SONDE</text>""" % {'x': -22+x, 'y': -52.4+y, 'text_color': colors['entity_cartouche_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">id_sonde</text>""" % {'x': -64+x, 'y': -26.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(stroke_color)s" stroke-width="1"/>""" % {'x0': -64+x, 'y0': -24.0+y, 'x1': 4+x, 'y1': -24.0+y, 'stroke_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">nom_sonde</text>""" % {'x': -64+x, 'y': -8.4+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">prenom_sonde</text>""" % {'x': -64+x, 'y': 9.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">sexe_sonde</text>""" % {'x': -64+x, 'y': 27.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">datenaiss_sonde</text>""" % {'x': -64+x, 'y': 45.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(text_color)s" font-family="Courier New" font-size="14">tel_sonde</text>""" % {'x': -64+x, 'y': 63.6+y, 'text_color': colors['entity_attribute_text_color']}
lines += u"""\n</g>""" % {}
lines += u'\n</svg>'

with codecs.open("mcdglobal_arranged.svg", "w", "utf8") as f:
    f.write(lines)
safe_print_for_PHP(u'Fichier de sortie "mcdglobal_arranged.svg" généré avec succès.')