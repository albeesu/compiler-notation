
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BARLINE BEAT CAPO CBYTE DSTART END HLOCTAVE MAJOR NUMBER OJUMP REDUCE REPEAT SEGNO SHARPFLATprogram : begin statementlist endbegin : MAJOR CBYTE BARLINEend : ENDstatementlist : expressionexpression : emptyexpression : music expressionmusic : REPEATmusic : BARLINE music : octave doremusic : dore notemusic : redu doremusic : doremusic : BEATmusic : dst expression SEGNOmusic : expression OJUMP dst : DSTARTmusic : expression CAPOdore : NUMBERoctave : HLOCTAVEredu : REDUCEnote : SHARPFLATempty :'
    
_lr_action_items = {'SHARPFLAT':([11,12,],[-18,25,]),'HLOCTAVE':([2,5,7,9,11,12,16,18,19,20,22,23,24,25,26,27,31,],[14,14,-13,-7,-18,-12,-16,14,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'REDUCE':([2,5,7,9,11,12,16,18,19,20,22,23,24,25,26,27,31,],[8,8,-13,-7,-18,-12,-16,8,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'DSTART':([2,5,7,9,11,12,16,18,19,20,22,23,24,25,26,27,31,],[16,16,-13,-7,-18,-12,-16,16,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'$end':([3,28,29,],[0,-1,-3,]),'BARLINE':([2,4,5,7,9,11,12,16,18,19,20,22,23,24,25,26,27,31,],[19,20,19,-13,-7,-18,-12,-16,19,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'MAJOR':([0,],[1,]),'REPEAT':([2,5,7,9,11,12,16,18,19,20,22,23,24,25,26,27,31,],[9,9,-13,-7,-18,-12,-16,9,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'OJUMP':([2,5,6,7,9,11,12,16,17,18,19,20,21,22,23,24,25,26,27,30,31,],[-22,-22,23,-13,-7,-18,-12,-16,-5,-22,-8,-2,23,-17,-15,-11,-21,-10,-9,23,-14,]),'CBYTE':([1,],[4,]),'NUMBER':([2,5,7,8,9,10,11,12,13,14,16,18,19,20,22,23,24,25,26,27,31,],[11,11,-13,-20,-7,11,-18,-12,11,-19,-16,11,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'BEAT':([2,5,7,9,11,12,16,18,19,20,22,23,24,25,26,27,31,],[7,7,-13,-7,-18,-12,-16,7,-8,-2,-17,-15,-11,-21,-10,-9,-14,]),'CAPO':([2,5,6,7,9,11,12,16,17,18,19,20,21,22,23,24,25,26,27,30,31,],[-22,-22,22,-13,-7,-18,-12,-16,-5,-22,-8,-2,22,-17,-15,-11,-21,-10,-9,22,-14,]),'END':([2,6,7,9,11,12,15,17,18,19,20,22,23,24,25,26,27,30,31,],[-22,-4,-13,-7,-18,-12,29,-5,-22,-8,-2,-17,-15,-11,-21,-10,-9,-6,-14,]),'SEGNO':([5,7,9,11,12,16,17,18,19,21,22,23,24,25,26,27,30,31,],[-22,-13,-7,-18,-12,-16,-5,-22,-8,31,-17,-15,-11,-21,-10,-9,-6,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'dst':([2,5,18,],[5,5,5,]),'end':([15,],[28,]),'expression':([2,5,18,],[6,21,30,]),'redu':([2,5,18,],[10,10,10,]),'program':([0,],[3,]),'dore':([2,5,10,13,18,],[12,12,24,27,12,]),'octave':([2,5,18,],[13,13,13,]),'empty':([2,5,18,],[17,17,17,]),'statementlist':([2,],[15,]),'note':([12,],[26,]),'begin':([0,],[2,]),'music':([2,5,18,],[18,18,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> begin statementlist end','program',3,'p_start','musicyacc.py',22),
  ('begin -> MAJOR CBYTE BARLINE','begin',3,'p_begin','musicyacc.py',38),
  ('end -> END','end',1,'p_end','musicyacc.py',42),
  ('statementlist -> expression','statementlist',1,'p_statementlist','musicyacc.py',46),
  ('expression -> empty','expression',1,'p_expressions','musicyacc.py',49),
  ('expression -> music expression','expression',2,'p_expression_music','musicyacc.py',52),
  ('music -> REPEAT','music',1,'p_expression_repeat','musicyacc.py',55),
  ('music -> BARLINE','music',1,'p_music_pitch','musicyacc.py',64),
  ('music -> octave dore','music',2,'p_music_octave','musicyacc.py',78),
  ('music -> dore note','music',2,'p_music_m','musicyacc.py',81),
  ('music -> redu dore','music',2,'p_music_reduce','musicyacc.py',84),
  ('music -> dore','music',1,'p_music_dore','musicyacc.py',87),
  ('music -> BEAT','music',1,'p_music_beat','musicyacc.py',90),
  ('music -> dst expression SEGNO','music',3,'p_mdcs','musicyacc.py',103),
  ('music -> expression OJUMP','music',2,'p_jump','musicyacc.py',110),
  ('dst -> DSTART','dst',1,'p_mdcsTWO','musicyacc.py',115),
  ('music -> expression CAPO','music',2,'p_music_dc','musicyacc.py',120),
  ('dore -> NUMBER','dore',1,'p_num','musicyacc.py',127),
  ('octave -> HLOCTAVE','octave',1,'p_octave','musicyacc.py',240),
  ('redu -> REDUCE','redu',1,'p_redu','musicyacc.py',256),
  ('note -> SHARPFLAT','note',1,'p_note','musicyacc.py',260),
  ('empty -> <empty>','empty',0,'p_empty','musicyacc.py',286),
]
