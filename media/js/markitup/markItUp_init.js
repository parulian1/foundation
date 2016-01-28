$(document).ready(function()    {
	var mySettings = {
	onShiftEnter:	{keepDefault:false, replaceWith:'<br />\n'},
	onCtrlEnter:	{keepDefault:false, openWith:'\n<p>', closeWith:'</p>\n'},
	onTab:			{keepDefault:false, openWith:'	 '},
	markupSet: [
		{name:'Heading 1', key:'1', openWith:'<h1(!( class="[![Class]!]")!)>', closeWith:'</h1>', placeHolder:'Your title here...' },
		{name:'Heading 2', key:'2', openWith:'<h2(!( class="[![Class]!]")!)>', closeWith:'</h2>', placeHolder:'Your title here...' },
		{name:'Heading 3', key:'3', openWith:'<h3(!( class="[![Class]!]")!)>', closeWith:'</h3>', placeHolder:'Your title here...' },
		{name:'Heading 4', key:'4', openWith:'<h4(!( class="[![Class]!]")!)>', closeWith:'</h4>', placeHolder:'Your title here...' },
		{name:'Heading 5', key:'5', openWith:'<h5(!( class="[![Class]!]")!)>', closeWith:'</h5>', placeHolder:'Your title here...' },
		{name:'Heading 6', key:'6', openWith:'<h6(!( class="[![Class]!]")!)>', closeWith:'</h6>', placeHolder:'Your title here...' },
		{name:'Paragraph', openWith:'<p(!( class="[![Class]!]")!)>', closeWith:'</p>' },
		{separator:'---------------'},
		{name:'Size', key:'S', openWith:'<font size=[![Text size]!]>', closeWith:'</font>',
		dropMenu :[
			{name:'Big', openWith:'<font size=200>', closeWith:'</font>' },
			{name:'Normal', openWith:'<font size=100>', closeWith:'</font>' },
			{name:'Small', openWith:'<font size=50>', closeWith:'</font>' }
		]},
		{separator:'---------------' },
		{name:'Bold', key:'B', openWith:'(!(<strong>|!|<b>)!)', closeWith:'(!(</strong>|!|</b>)!)' },
		{name:'Italic', key:'I', openWith:'(!(<em>|!|<i>)!)', closeWith:'(!(</em>|!|</i>)!)' },
		{name:'Stroke through', key:'S', openWith:'<del>', closeWith:'</del>' },
		{name:'Underline', key:'U', openWith:'[u]', closeWith:'[/u]'},
		{separator:'---------------' },
		{name:'Ul', openWith:'<ul>\n', closeWith:'</ul>\n' },
		{name:'Ol', openWith:'<ol>\n', closeWith:'</ol>\n' },
		{name:'Li', openWith:'<li>', closeWith:'</li>' },
		{separator:'---------------' },
		{name:'Picture', key:'P', replaceWith:'<img src="[![Source:!:http://]!]" alt="[![Alternative text]!]" />' },
		{name:'Link', key:'L', openWith:'<a href="[![Link:!:http://]!]"(!( title="[![Title]!]")!)>', closeWith:'</a>', placeHolder:'Your text to link...' },
		{name:'Url', openWith:"[[![Url:!:http://]!] ", closeWith:']', placeHolder:'Your text to link here...' },
		{name:'Quotes', openWith:'(!(> |!|>)!)', placeHolder:''},
		{separator:'---------------' },
		{name:'Lowercase', className:'lowercase', key:'L', openWith:'<sub>', closeWith:'</sub>'},
		{name:'Uppercase', className:'uppercase', key:'U', openWith:'<sup>', closeWith:'</sup>'},
		{separator:'---------------' },
		{name:'Text indent', className:'indent', openWith:'text-indent:', placeHolder:'5px', closeWith:';' },
		{name:'Letter spacing', className:'letterspacing', openWith:'letter-spacing:', placeHolder:'5px', closeWith:';' },
		{name:'Line height', className:'lineheight', openWith:'<p style="line-height:1.5;">', closeWith:'</p>' },

		{separator:'---------------' },
		{name:'Background Image', className:'background', replaceWith:'background:url([![Source:!:http://]!]) no-repeat 0 0;' },
		{separator:'---------------' },
		
		{name:'Margin', className:'padding', dropMenu:[
				{name:'Top', className:'top', openWith:'<p style="margin-top:5px;">', closeWith:'</p>' },
				{name:'Left', className:'left', openWith:'<p style="margin-left:5px;">', closeWith:'</p>'},
				{name:'Right', className:'right', openWith:'<p style="margin-right:5px;">', closeWith:'</p>'},
				{name:'Bottom', className:'bottom', openWith:'<p style="margin-bottom:5px;">', closeWith:'</p>'}
			]
		},
		{name:'Alignments', className:'alignments', dropMenu:[
			{name:'Left', className:'left', openWith:'<p style="text-align:left;">', closeWith:'</p>'},
			{name:'Center', className:'center', openWith:'<p style="text-align:center;">', closeWith:'</p>'},
			{name:'Right', className:'right', openWith:'<p style="text-align:right;">', closeWith:'</p>'},
			{name:'Justify', className:'justify', openWith:'<p style="text-align:justify;">', closeWith:'</p>'}
			]
		},
		{separator:'---------------' },
		{name:'Clean', className:'clean', replaceWith:function(markitup) { return markitup.selection.replace(/<(.*?)>/g, "") } },
		{name:'Preview', className:'preview', call:'preview' },
	]
}
    $('textarea').markItUp(mySettings);
});