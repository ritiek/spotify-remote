If $CmdLineRaw = 'play/pause' Then				; if arguments passed to this script is 'play/pause'
   ControlSend('Spotify', '', '', '{space}')
   ;Send("{MEDIA_PLAY_PAUSE}")					; this is commented because it would also pause WMediaPlayer.. we want only spotify
ElseIf $CmdLineRaw = 'up' Then
   ControlSend('Spotify', '', '', '^{up}')
   ControlSend('Spotify', '', '', '^{up}')
ElseIf $CmdLineRaw = 'down' Then
   ControlSend('Spotify', '', '', '^{down}')
   ControlSend('Spotify', '', '', '^{down}')
ElseIf $CmdLineRaw = 'prev' Then
   ControlSend('Spotify', '', '', '^{left}')
ElseIf $CmdLineRaw = 'next' Then
   ControlSend('Spotify', '', '', '^{right}')
ElseIf $CmdLineRaw = 'repeat' Then
   ControlSend('Spotify', '', '', '^r')
EndIf