// JavaScript Document
$(function () {  
		$('.Choicesnext').click(function () {  
			$(".Choices_banner ul").animate({marginLeft:"-1184px"},600, function () {  
				$(".Choices_banner ul>li").eq(0).appendTo($(".Choices_banner ul"));  
				$(".Choices_banner ul").css('marginLeft','0px');  
			});  
			$(".Choicestel ul").css('marginLeft','-1184px');  
			$(".Choicestel ul>li").eq(0).appendTo($(".Choicestel ul"));  
			$(".Choicestel ul").css({marginLeft:"0px"},600);
		})  
		/*$('.Choicesprev').click(function () {  
			$(".Choices_banner ul").css('marginLeft','-1184px');  
			$(".Choices_banner ul>li").eq(3).prependTo($(".Choices_banner ul"));  
			$(".Choices_banner ul").animate({marginLeft:"0px"},600);  
			$(".Choicestel ul").css('marginLeft','-1184px');  
			$(".Choicestel ul>li").eq(3).prependTo($(".Choicestel ul"));  
			$(".Choicestel ul").css({marginLeft:"0px"},600);  
		})  */
	})
	  
$(function(){	
	function Choices(){
		$(".Choices_banner ul").animate({marginLeft:"-1184px"},600, function () {  
					$(".Choices_banner ul>li").eq(0).appendTo($(".Choices_banner ul"));  
					$(".Choices_banner ul").css('marginLeft','0px');  
				});  
				$(".Choicestel ul").css('marginLeft','-1184px');  
				$(".Choicestel ul>li").eq(0).appendTo($(".Choicestel ul"));  
				$(".Choicestel ul").css({marginLeft:"0px"},600);
		}
	setInterval("Choices()","100000");
	var tabChange = setInterval(Choices,100000);
		//鼠标悬停暂停切换
		$('.Choicesnext').mouseover(function(){
			clearInterval(tabChange);
		});
		$('.Choicesnext').mouseout(function(){
			tabChange = setInterval(Choices,100000);
		});
})
