<template>
<div class="home-preview" :style='{"width":"100%","margin":"0px auto","flexWrap":"wrap","justifyContent":"center","display":"flex"}'>
	<el-row type="flex" :gutter="5" justify="center" style="width: 100%">
		<el-col :span="3" v-if="queryList.length>1">
			<el-select v-model="queryIndex">
				<el-option
				  v-for="(item,index) in queryList"
				  :key="index"
				  :label="item.queryName"
				  :value="index"
				></el-option>
			</el-select>
		</el-col>
		<el-col :span="3" v-if="queryIndex==0">
			<el-input v-model="xinwenzixunbiaoti" placeholder="标题"></el-input>
		</el-col>
		<el-col :span="3" v-if="queryIndex==0">
			<el-button type="primary" @click="search('xinwenzixun')">搜索</el-button>
		</el-col>
	</el-row>


	<!-- 关于我们 -->
	<div :style='{"padding":"40px 20px","boxShadow":"0 0px 0px rgba(255, 255, 255, .3)","margin":"40px 7% 0","background":"#f6f5f3","display":"block","width":"86%","position":"relative","height":"auto","order":"1"}'>
	  <div :style='{"padding":"0 40px","color":"#333","top":"100px","textAlign":"left","left":"50%","width":"auto","lineHeight":"40px","fontSize":"24px","position":"absolute","fontWeight":"500","order":"1"}'>{{aboutUsDetail.title}}</div>
	  <div :style='{"padding":"0 40px","margin":"0","color":"#555","textAlign":"left","display":"inline-block","top":"120px","left":"50%","width":"auto","lineHeight":"60px","fontSize":"18px","position":"absolute","zIndex":"9","order":"2","height":"66px"}'>{{aboutUsDetail.subtitle}}</div>
	  <div :style='{"padding":"0","display":"block","width":"50%","position":"relative","float":"left","height":"450px","order":"2"}'>
	    <img :style='{"margin":"0","objectFit":"cover","flex":1,"background":"#fff","display":"block","width":"100%","height":"100%"}' :src="baseUrl + aboutUsDetail.picture1">
	    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + aboutUsDetail.picture2">
	    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + aboutUsDetail.picture3">
	  </div>
	  <div :style='{"padding":"100px 20px 0 40px","margin":"40px 0 0","borderColor":"#C9A984","color":"#333","textIndent":"2em","float":"right","overflow":"hidden","background":"url(http://codegen.caihongy.cn/20230207/bbae85c30f0d4116bd96ad1da43bd908.png) no-repeat left top,url(http://codegen.caihongy.cn/20230207/b2a2e3d0cd374cc79f6d3942ddc89032.png) no-repeat right top,url(http://codegen.caihongy.cn/20230207/f085b37fc41647baaade291478fd776a.png) no-repeat left bottom,url(http://codegen.caihongy.cn/20230207/abd32f342140451893cd2d99e0f92e53.png) no-repeat right bottom,#fff","borderWidth":"1px 1px 1px 0","width":"50%","lineHeight":"24px","fontSize":"14px","borderStyle":"outset","height":"370px","order":"3"}' v-html="aboutUsDetail.content"></div>
	  <div :style='{"top":"183px","background":"url(http://codegen.caihongy.cn/20230207/90986aaa115f4047afc8fce7d329dca7.png) no-repeat left top","display":"block","width":"50%","position":"absolute","right":"10px","height":"450px","zIndex":"9"}' />
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	</div>
	<!-- 系统简介 -->
	<div :style='{"padding":"0 0 80px","boxShadow":"0 0px 0px rgba(255, 255, 255, .3)","margin":"40px 7% 0 0","flexWrap":"wrap","background":"none","display":"flex","width":"23%","position":"relative","height":"auto","order":"20"}'>
	  <div :style='{"padding":"0 20px 0 100px","borderColor":"#7e6b5a","color":"#4e4e4e","textAlign":"left","float":"left","outline":"1px solid #7e6b5a","outlineOffset":"2px","background":"url(http://codegen.caihongy.cn/20230207/cb0df322e9b14cb3b11556207d9fab2b.png) no-repeat 20px -1px,#f6f5f3","borderWidth":"1px 0","width":"100%","lineHeight":"56px","fontSize":"18px","borderStyle":"dashed","fontWeight":"600","height":"56px"}'>{{systemIntroductionDetail.title}}</div>
	  <div :style='{"margin":"0","color":"#4e4e4e","textAlign":"left","display":"none","width":"50%","lineHeight":"56px","fontSize":"16px"}'>{{systemIntroductionDetail.subtitle}}</div>
	  <div :style='{"width":"100%","padding":"0 0","margin":"20px 0 0","display":"block","height":"240px"}'>
	    <img :style='{"padding":"30px 20px","margin":"0","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","display":"block","width":"100%","height":"100%"}' :src="baseUrl + systemIntroductionDetail.picture1">
	    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + systemIntroductionDetail.picture2">
	    <img :style='{"margin":"0 10px","objectFit":"cover","flex":1,"display":"none","height":"120px"}' :src="baseUrl + systemIntroductionDetail.picture3">
	  </div>
	  <div :style='{"padding":"20px","margin":"0","overflow":"hidden","color":"#333","width":"100%","lineHeight":"24px","fontSize":"14px","position":"relative","textIndent":"2em","height":"186px","zIndex":"99"}' v-html="systemIntroductionDetail.content"></div>
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	  <div :style='{"width":"285px","background":"url(\"http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg\") 0% 0% / cover no-repeat","display":"none","height":"100px"}' />
	</div>

<div class="recommend" :style='{"padding":"20px 7% 0","margin":"0","textAlign":"center","background":"none","display":"block","width":"100%","position":"relative","order":"2"}'>
	
    <div class="title" :style='{"margin":"20px auto 40px","borderColor":"#7e6b5a","outline":"1px solid #7e6b5a","alignItems":"flex-start","outlineOffset":"2px","background":"#f6f5f3","borderWidth":"1px 0","display":"flex","width":"auto","position":"relative","borderStyle":"dashed","height":"56px"}'>
		<span :style='{"padding":"0 20px 0 100px","fontSize":"18px","lineHeight":"54px","color":"#4e4e4e","background":"url(http://codegen.caihongy.cn/20230207/cb0df322e9b14cb3b11556207d9fab2b.png) no-repeat 20px -1px,#f6f5f3","fontWeight":"600"}'>新闻资讯推荐</span>
	</div>
	
	<div v-if="true" class="idea recommendIdea" :style='{"padding":"0","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20230208/7ff655a2b70d4061a845fc8af0bee79d.jpg) no-repeat left center / 100% 100%","display":"flex","width":"100%","justifyContent":"space-between","height":"240px"}'>
		<div class="box1" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	
	
	
	<!-- 样式四 -->
	<div class="list list4 index-pv1" :style='{"minHeight":"760px","width":"100%","padding":"40px 0 0","background":"none","display":"block","height":"auto"}'>
		<div v-if="xinwenzixunRecommend.length>0" class="list-item animation-box" @click="toDetail('xinwenzixunDetail', xinwenzixunRecommend[0])" :style='{"cursor":"pointer","width":"20%","margin":"0","position":"relative","float":"right","height":"480px"}'>
			<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-if="preHttp(xinwenzixunRecommend[0].fengmian)" :src="xinwenzixunRecommend[0].fengmian.split(',')[0]" alt="" />
			<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-else :src="baseUrl + (xinwenzixunRecommend[0].fengmian?xinwenzixunRecommend[0].fengmian.split(',')[0]:'')" alt="" />
			<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                <div>{{xinwenzixunRecommend[0].biaoti}}</div>
                <div>{{xinwenzixunRecommend[0].xinwenleixing}}</div>
            </div>
		</div>
		<div class="list-body" :style='{"width":"40%","margin":"0","float":"left","justifyContent":"space-between","display":"flex","height":"480px"}'>
			<div v-if="xinwenzixunRecommend.length>1" @click="toDetail('xinwenzixunDetail', xinwenzixunRecommend[1])" class="list-item animation-box" :style='{"width":"50%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-if="preHttp(xinwenzixunRecommend[1].fengmian)" :src="xinwenzixunRecommend[1].fengmian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-else :src="baseUrl + (xinwenzixunRecommend[1].fengmian?xinwenzixunRecommend[1].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunRecommend[1].biaoti}}</div>
                    <div>{{xinwenzixunRecommend[1].xinwenleixing}}</div>
                </div>
			</div>
			<div v-if="xinwenzixunRecommend.length>2" @click="toDetail('xinwenzixunDetail', xinwenzixunRecommend[2])" class="list-item animation-box" :style='{"width":"50%","margin":"80px 0 0","position":"relative","flexWrap":"wrap","display":"flex","height":"100%"}'>
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-if="preHttp(xinwenzixunRecommend[2].fengmian)" :src="xinwenzixunRecommend[2].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-else :src="baseUrl + (xinwenzixunRecommend[2].fengmian?xinwenzixunRecommend[2].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunRecommend[2].biaoti}}</div>
                    <div>{{xinwenzixunRecommend[2].xinwenleixing}}</div>
                </div>
			</div>
		</div>
		<div class="list-body" :style='{"width":"40%","margin":"0","float":"left","justifyContent":"space-between","display":"flex","height":"480px"}'>
			<div v-if="xinwenzixunRecommend.length>3" @click="toDetail('xinwenzixunDetail', xinwenzixunRecommend[3])" class="list-item animation-box" :style='{"width":"50%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-if="preHttp(xinwenzixunRecommend[3].fengmian)" :src="xinwenzixunRecommend[3].fengmian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-else :src="baseUrl + (xinwenzixunRecommend[3].fengmian?xinwenzixunRecommend[3].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunRecommend[3].biaoti}}</div>
                    <div>{{xinwenzixunRecommend[3].xinwenleixing}}</div>
                </div>
			</div>
			<div v-if="xinwenzixunRecommend.length>4" @click="toDetail('xinwenzixunDetail', xinwenzixunRecommend[4])" class="list-item animation-box" :style='{"width":"50%","margin":"80px 0 0","position":"relative","flexWrap":"wrap","display":"flex","height":"100%"}'>
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-if="preHttp(xinwenzixunRecommend[4].fengmian)" :src="xinwenzixunRecommend[4].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-else :src="baseUrl + (xinwenzixunRecommend[4].fengmian?xinwenzixunRecommend[4].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunRecommend[4].biaoti}}</div>
                    <div>{{xinwenzixunRecommend[4].xinwenleixing}}</div>
                </div>
			</div>
		</div>
	</div>
	
	
	
	
	
	
	<div @click="moreBtn('xinwenzixun')" :style='{"border":"0","padding":"0 2px 0 10px","margin":"20px auto","textAlign":"center","display":"inline-block","minWidth":"120px","right":"calc(7% + 20px)","borderRadius":"8px","top":"28px","background":"none","width":"auto","lineHeight":"40px","position":"absolute","height":"44px","zIndex":"1010"}'>
		<span :style='{"color":"#333","fontSize":"15px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#333","fontSize":"15px"}' class="el-icon-d-arrow-right"></i>
	</div>
	
</div>
<div class="recommend" :style='{"padding":"20px 7% 0","margin":"0","textAlign":"center","background":"none","display":"block","width":"100%","position":"relative","order":"2"}'>
	
    <div class="title" :style='{"margin":"20px auto 40px","borderColor":"#7e6b5a","outline":"1px solid #7e6b5a","alignItems":"flex-start","outlineOffset":"2px","background":"#f6f5f3","borderWidth":"1px 0","display":"flex","width":"auto","position":"relative","borderStyle":"dashed","height":"56px"}'>
		<span :style='{"padding":"0 20px 0 100px","fontSize":"18px","lineHeight":"54px","color":"#4e4e4e","background":"url(http://codegen.caihongy.cn/20230207/cb0df322e9b14cb3b11556207d9fab2b.png) no-repeat 20px -1px,#f6f5f3","fontWeight":"600"}'>网易新闻推荐</span>
	</div>
	
	<div v-if="true" class="idea recommendIdea" :style='{"padding":"0","flexWrap":"wrap","background":"url(http://codegen.caihongy.cn/20230208/7ff655a2b70d4061a845fc8af0bee79d.jpg) no-repeat left center / 100% 100%","display":"flex","width":"100%","justifyContent":"space-between","height":"240px"}'>
		<div class="box1" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"0","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	
	
	
	<!-- 样式四 -->
	<div class="list list4 index-pv1" :style='{"minHeight":"760px","width":"100%","padding":"40px 0 0","background":"none","display":"block","height":"auto"}'>
		<div v-if="wangyixinwenRecommend.length>0" class="list-item animation-box" @click="toDetail('wangyixinwenDetail', wangyixinwenRecommend[0])" :style='{"cursor":"pointer","width":"20%","margin":"0","position":"relative","float":"right","height":"480px"}'>
			<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-if="preHttp(wangyixinwenRecommend[0].fengmian)" :src="wangyixinwenRecommend[0].fengmian.split(',')[0]" alt="" />
			<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-else :src="baseUrl + (wangyixinwenRecommend[0].fengmian?wangyixinwenRecommend[0].fengmian.split(',')[0]:'')" alt="" />
			<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                <div>{{wangyixinwenRecommend[0].biaoti}}</div>
                <div>{{wangyixinwenRecommend[0].guanjianzi}}</div>
                <div>发布时间:{{wangyixinwenRecommend[0].fabushijian}}</div>
            </div>
		</div>
		<div class="list-body" :style='{"width":"40%","margin":"0","float":"left","justifyContent":"space-between","display":"flex","height":"480px"}'>
			<div v-if="wangyixinwenRecommend.length>1" @click="toDetail('wangyixinwenDetail', wangyixinwenRecommend[1])" class="list-item animation-box" :style='{"width":"50%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-if="preHttp(wangyixinwenRecommend[1].fengmian)" :src="wangyixinwenRecommend[1].fengmian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-else :src="baseUrl + (wangyixinwenRecommend[1].fengmian?wangyixinwenRecommend[1].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{wangyixinwenRecommend[1].biaoti}}</div>
                    <div>{{wangyixinwenRecommend[1].guanjianzi}}</div>
                    <div>发布时间:{{wangyixinwenRecommend[1].fabushijian}}</div>
                </div>
			</div>
			<div v-if="wangyixinwenRecommend.length>2" @click="toDetail('wangyixinwenDetail', wangyixinwenRecommend[2])" class="list-item animation-box" :style='{"width":"50%","margin":"80px 0 0","position":"relative","flexWrap":"wrap","display":"flex","height":"100%"}'>
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-if="preHttp(wangyixinwenRecommend[2].fengmian)" :src="wangyixinwenRecommend[2].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-else :src="baseUrl + (wangyixinwenRecommend[2].fengmian?wangyixinwenRecommend[2].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{wangyixinwenRecommend[2].biaoti}}</div>
                    <div>{{wangyixinwenRecommend[2].guanjianzi}}</div>
                    <div>发布时间:{{wangyixinwenRecommend[2].fabushijian}}</div>
                </div>
			</div>
		</div>
		<div class="list-body" :style='{"width":"40%","margin":"0","float":"left","justifyContent":"space-between","display":"flex","height":"480px"}'>
			<div v-if="wangyixinwenRecommend.length>3" @click="toDetail('wangyixinwenDetail', wangyixinwenRecommend[3])" class="list-item animation-box" :style='{"width":"50%","margin":"0","position":"relative","display":"inline-block","height":"100%"}'>
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-if="preHttp(wangyixinwenRecommend[3].fengmian)" :src="wangyixinwenRecommend[3].fengmian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","padding":"50px 30px","objectFit":"cover","float":"left","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","height":"100%"}' v-else :src="baseUrl + (wangyixinwenRecommend[3].fengmian?wangyixinwenRecommend[3].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{wangyixinwenRecommend[3].biaoti}}</div>
                    <div>{{wangyixinwenRecommend[3].guanjianzi}}</div>
                    <div>发布时间:{{wangyixinwenRecommend[3].fabushijian}}</div>
                </div>
			</div>
			<div v-if="wangyixinwenRecommend.length>4" @click="toDetail('wangyixinwenDetail', wangyixinwenRecommend[4])" class="list-item animation-box" :style='{"width":"50%","margin":"80px 0 0","position":"relative","flexWrap":"wrap","display":"flex","height":"100%"}'>
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-if="preHttp(wangyixinwenRecommend[4].fengmian)" :src="wangyixinwenRecommend[4].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"50px 30px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"100%","order":"2"}' v-else :src="baseUrl + (wangyixinwenRecommend[4].fengmian?wangyixinwenRecommend[4].fengmian.split(',')[0]:'')" alt="" />
				<div class="title line1" :style='{"margin":"0 auto","whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"80%","lineHeight":"44px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{wangyixinwenRecommend[4].biaoti}}</div>
                    <div>{{wangyixinwenRecommend[4].guanjianzi}}</div>
                    <div>发布时间:{{wangyixinwenRecommend[4].fabushijian}}</div>
                </div>
			</div>
		</div>
	</div>
	
	
	
	
	
	
	<div @click="moreBtn('wangyixinwen')" :style='{"border":"0","padding":"0 2px 0 10px","margin":"20px auto","textAlign":"center","display":"inline-block","minWidth":"120px","right":"calc(7% + 20px)","borderRadius":"8px","top":"28px","background":"none","width":"auto","lineHeight":"40px","position":"absolute","height":"44px","zIndex":"1010"}'>
		<span :style='{"color":"#333","fontSize":"15px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#333","fontSize":"15px"}' class="el-icon-d-arrow-right"></i>
	</div>
	
</div>

	
<div class="news" :style='{"padding":"0 7%","margin":"40px 0 0","flexWrap":"wrap","background":"none","flex":"1","display":"flex","width":"100%","position":"relative","order":"3"}'>
	<div v-if="false" class="idea newsIdea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"margin":"0 auto 20px","borderColor":"#7e6b5a","textAlign":"center","display":"flex","outline":"1px solid #7e6b5a","top":"0","outlineOffset":"2px","background":"#f6f5f3","borderWidth":"1px 0","width":"100%","position":"relative","borderStyle":"dashed","zIndex":"99","height":"56px"}'>
		<span :style='{"padding":"0 20px 0 100px","margin":"0 10px 0 0","color":"#4e4e4e","textAlign":"center","background":"url(http://codegen.caihongy.cn/20230207/cb0df322e9b14cb3b11556207d9fab2b.png) no-repeat 20px -1px,#f6f5f3","width":"auto","fontSize":"18px","lineHeight":"56px","fontWeight":"600"}'>资讯</span>
	</div>
	
	
	
	
	
	
	
	
	
	
	
	<!-- 样式十 -->
	<div v-if="newsList.length" class="list list10 index-pv1" :style='{"padding":"0","flexWrap":"wrap","background":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
	  <div v-if="newsList.length>0" @click="toDetail('newsDetail', newsList[0])" :style='{"width":"48%","margin":"0","position":"relative","background":"none","height":"auto"}' class="new10-list-item animation-box">
	    <img :style='{"width":"100%","objectFit":"cover","display":"block","height":"290px"}' :src="baseUrl + newsList[0].picture" alt="">
		<div :style='{"padding":"0 20px","margin":"20px 100px 0 0","whiteSpace":"nowrap","overflow":"hidden","color":"#333","background":"#fff","width":"calc(100% - 100px)","fontSize":"16px","lineHeight":"40px","textOverflow":"ellipsis","fontWeight":"500"}' class="new9-list-item-title line1">{{newsList[0].title}}</div>
		<div :style='{"color":"#a6937c","borderRadius":"100%","textAlign":"center","bottom":"23px","background":"radial-gradient(circle, rgba(255,255,255,1) 23%, rgba(233,228,218,1) 100%),#f6f5f3","width":"100px","fontSize":"14px","lineHeight":"100px","position":"absolute","right":"0","height":"100px"}' class="new9-list-item-time">{{newsList[0].addtime.split(' ')[0]}}</div>
	    <div :style='{"padding":"0 20px","margin":"0 100px 0 0","overflow":"hidden","color":"#555","background":"#fff","width":"calc(100% - 100px)","fontSize":"14px","lineHeight":"30px","textIndent":"2em","height":"60px"}' class="new9-list-item-descript line2">{{newsList[0].introduction}}</div>
		<div :style='{"padding":"0 10px","margin":"0 10px 10px","color":"#999","background":"#fff","display":"none","fontSize":"12px","lineHeight":"24px"}' class="new9-list-item-identification">新闻动态</div>
	  </div>
	  <div v-if="newsList.length>1" :style='{"width":"48%","margin":"0","position":"relative","background":"none","display":"block","height":"400px"}'>
	    <div v-for="(item,index) in newsList" v-if="index<4 && index>0" :key="index" @click="toDetail('newsDetail', item)" :style='{"width":"100%","padding":"0 120px 0 0","margin":"0 0 55px","position":"relative","background":"#fff","height":"100px"}' class="new10-list-item animation-box">
	        <div :style='{"padding":"10px 0 0","whiteSpace":"nowrap","overflow":"hidden","color":"#333","width":"calc(100% - 20px)","fontSize":"16px","lineHeight":"1","textOverflow":"ellipsis","fontWeight":"500"}' class="new9-list-item-title line1">{{ item.title }}</div>
	        <div :style='{"color":"#a6937c","top":"0","borderRadius":"100%","textAlign":"center","background":"radial-gradient(circle, rgba(255,255,255,1) 23%, rgba(233,228,218,1) 100%),#f6f5f3","width":"100px","fontSize":"14px","lineHeight":"100px","position":"absolute","right":"0","height":"100px"}' class="new9-list-item-time">{{ item.addtime.split(' ')[0] }}</div>
			<div :style='{"padding":"0 20px 0 0","margin":"5px auto 0","overflow":"hidden","color":"#555","display":"block","width":"100%","fontSize":"14px","lineHeight":"30px","textIndent":"2em","height":"60px"}' class="new9-list-item-descript line2">{{ item.introduction }}</div>
			<div :style='{"padding":"0 10px","fontSize":"12px","lineHeight":"24px","color":"#999","background":"#fff","display":"none"}' class="new9-list-item-identification">新闻动态</div>
	    </div>
	  </div>
	</div>
	
	<div @click="moreBtn('news')" :style='{"border":"0","padding":"0 12px 0 20px","margin":"0 auto","textAlign":"center","display":"inline-block","minWidth":"120px","right":"calc(7% + 40px)","borderRadius":"8px","top":"8px","background":"none","width":"auto","lineHeight":"40px","position":"absolute","height":"44px","zIndex":"1010"}'>
		<span :style='{"color":"#333","fontSize":"15px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#333","fontSize":"15px"}' class="el-icon-d-arrow-right"></i>
	</div>
	
</div>


<div class="lists" :style='{"padding":"0 0 60px","margin":"60px 7% 0","textAlign":"center","background":"none","display":"block","width":"86%","position":"relative","order":"30"}'>
	<div v-if="false" class="idea" :style='{"padding":"20px","flexWrap":"wrap","background":"#efefef","justifyContent":"space-between","display":"flex"}'>
		<div class="box1" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"margin":"0 0 40px","borderColor":"#7e6b5a","alignItems":"flex-start","textAlign":"center","display":"flex","outline":"1px solid #7e6b5a","outlineOffset":"2px","background":"#f6f5f3","borderWidth":"1px 0","width":"auto","position":"relative","borderStyle":"dashed","height":"56px"}'>
	  <span :style='{"padding":"0 20px 0 100px","fontSize":"18px","lineHeight":"54px","color":"#4e4e4e","background":"url(http://codegen.caihongy.cn/20230207/cb0df322e9b14cb3b11556207d9fab2b.png) no-repeat 20px -1px,#f6f5f3","fontWeight":"600"}'>新闻资讯展示</span>
	</div>
	
	
	
	
	
	
	
	
	
	<!-- 样式八 -->
	<div class="list list8 index-pv1" :style='{"padding":"0","flexWrap":"wrap","background":"#fff","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
		<div :style='{"width":"48%","flexWrap":"wrap","justifyContent":"space-between","display":"flex","height":"570px","order":"2"}' class="list-body">
			<div v-if="xinwenzixunList.length>0" @click="toDetail('xinwenzixunDetail', xinwenzixunList[0])" class="list-4-item animation-box item-1" :style='{"width":"48%","margin":"0","position":"relative","height":"auto","order":"2"}'>
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-if="preHttp(xinwenzixunList[0].fengmian)" :src="xinwenzixunList[0].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-else :src="baseUrl + (xinwenzixunList[0].fengmian?xinwenzixunList[0].fengmian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"100%","lineHeight":"30px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunList[0].biaoti}}</div>
                    <div>{{xinwenzixunList[0].xinwenleixing}}</div>
                </div>
			</div>
			<div v-if="xinwenzixunList.length>1" @click="toDetail('xinwenzixunDetail', xinwenzixunList[1])" class="list-4-item animation-box item-2" :style='{"width":"48%","margin":"0","position":"relative","height":"auto","order":"3"}'>
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-if="preHttp(xinwenzixunList[1].fengmian)" :src="xinwenzixunList[1].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-else :src="baseUrl + (xinwenzixunList[1].fengmian?xinwenzixunList[1].fengmian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"100%","lineHeight":"30px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunList[1].biaoti}}</div>
                    <div>{{xinwenzixunList[1].xinwenleixing}}</div>
                </div>
			</div>
			<div v-if="xinwenzixunList.length>2" @click="toDetail('xinwenzixunDetail', xinwenzixunList[2])" class="list-4-item animation-box item-3" :style='{"width":"100%","margin":"0 0 20px","position":"relative","height":"auto"}'>
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-if="preHttp(xinwenzixunList[2].fengmian)" :src="xinwenzixunList[2].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-else :src="baseUrl + (xinwenzixunList[2].fengmian?xinwenzixunList[2].fengmian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"100%","lineHeight":"30px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunList[2].biaoti}}</div>
                    <div>{{xinwenzixunList[2].xinwenleixing}}</div>
                </div>
			</div>
		</div>
		<div :style='{"width":"48%","margin":"0","flexWrap":"wrap","justifyContent":"space-between","display":"flex","height":"auto"}' class="list-body">
			<div v-if="xinwenzixunList.length>3" @click="toDetail('xinwenzixunDetail', xinwenzixunList[3])" class="list-4-item animation-box item-4" :style='{"width":"100%","margin":"0 0 20px","position":"relative","height":"auto"}'>
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-if="preHttp(xinwenzixunList[3].fengmian)" :src="xinwenzixunList[3].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-else :src="baseUrl + (xinwenzixunList[3].fengmian?xinwenzixunList[3].fengmian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"100%","lineHeight":"30px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunList[3].biaoti}}</div>
                    <div>{{xinwenzixunList[3].xinwenleixing}}</div>
                </div>
			</div>
			<div v-if="xinwenzixunList.length>4" @click="toDetail('xinwenzixunDetail', xinwenzixunList[4])" class="list-4-item animation-box item-5" :style='{"width":"100%","position":"relative","height":"auto"}'>
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-if="preHttp(xinwenzixunList[4].fengmian)" :src="xinwenzixunList[4].fengmian.split(',')[0]" alt="" />
				<img :style='{"padding":"40px","margin":"0 0 4px","objectFit":"cover","background":"url(http://codegen.caihongy.cn/20230207/346e413dce8f4515a5a57219df032ccd.png) no-repeat left top / auto 100%,url(http://codegen.caihongy.cn/20230207/e75d04594fa6401b9993f023e829f7b8.png) no-repeat right bottom / auto 100%","width":"100%","float":"left","height":"400px"}' v-else :src="baseUrl + (xinwenzixunList[4].fengmian?xinwenzixunList[4].fengmian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#fff","textAlign":"center","background":"linear-gradient(270deg, rgba(255,255,255,1) 0%, rgba(207,193,176,1) 20%, rgba(166,147,124,1) 50%, rgba(207,193,176,1) 80%, rgba(255,255,255,1) 100%),#a6937c","width":"100%","lineHeight":"30px","fontSize":"14px","textOverflow":"ellipsis"}'>
                    <div>{{xinwenzixunList[4].biaoti}}</div>
                    <div>{{xinwenzixunList[4].xinwenleixing}}</div>
                </div>
			</div>
		</div>
	</div>
	
	
	<div @click="moreBtn('xinwenzixun')" :style='{"border":"0","padding":"0 20px","margin":"0 auto","textAlign":"center","display":"block","minWidth":"120px","right":"0","borderRadius":"8px","top":"8px","background":"none","width":"auto","lineHeight":"40px","position":"absolute","zIndex":"1010"}'>
		<span :style='{"color":"#333","fontSize":"15px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#333","fontSize":"15px"}' class="el-icon-d-arrow-right"></i>
	</div>
	

</div>


</div>
</template>

<script>
  export default {
    //数据集合
    data() {
      return {
        baseUrl: '',
        aboutUsDetail: {},
        systemIntroductionDetail: {},
        queryList:[
          {
              queryName:"标题",
          },
        ],
        queryIndex: 0,
        xinwenzixunbiaoti: '',
        newsList: [],
        xinwenzixunRecommend: [],
        wangyixinwenRecommend: [],

        xinwenzixunList: [],
      }
    },
    created() {
      this.baseUrl = this.$config.baseUrl;
      this.getNewsList();
      this.getAboutUs();
      this.getSystemIntroduction();
      this.getList();
    },
    //方法集合
    methods: {
      preHttp(str) {
          return str && str.substr(0,4)=='http';
      },
      getAboutUs() {
          this.$http.get('aboutus/detail/1', {}).then(res => {
            if(res.data.code == 0) {
              this.aboutUsDetail = res.data.data;
            }
          })
      },
      getSystemIntroduction() {
          this.$http.get('systemintro/detail/1', {}).then(res => {
            if(res.data.code == 0) {
              this.systemIntroductionDetail = res.data.data;
            }
          })
      },
      search(tablename) {
        if (this.queryIndex == 0 && this.xinwenzixunbiaoti) {
          this.$router.push({path: '/index/' + tablename, query: {indexQueryCondition: this.xinwenzixunbiaoti}});
        }
      },
		getNewsList() {
			this.$http.get('news/list', {params: {
				page: 1,
				limit: 4,
			order: 'desc'}}).then(res => {
				if (res.data.code == 0) {
					this.newsList = res.data.data.list;
					
					
				}
			});
		},
		getList() {
          let autoSortUrl = "";
          autoSortUrl = "xinwenzixun/autoSort";
          if(localStorage.getItem('Token')) {
              autoSortUrl = "xinwenzixun/autoSort2";
          }
			this.$http.get(autoSortUrl, {params: {
				page: 1,
				limit: 5,
			}}).then(res => {
				if (res.data.code == 0) {
					this.xinwenzixunRecommend = res.data.data.list;
					
					
					// 商品列表样式五
					
				}
			});
          autoSortUrl = "wangyixinwen/autoSort";
			this.$http.get(autoSortUrl, {params: {
				page: 1,
				limit: 5,
			}}).then(res => {
				if (res.data.code == 0) {
					this.wangyixinwenRecommend = res.data.data.list;
					
					
					// 商品列表样式五
					
				}
			});
			
			this.$http.get('xinwenzixun/list', {params: {
				sort : 'fabushijian',
				order: 'desc',
				page: 1,
				limit: 5,
			}}).then(res => {
				if (res.data.code == 0) {
					this.xinwenzixunList = res.data.data.list;
					
					// 商品列表样式五
					
				}
			});
		},
		toDetail(path, item) {
			this.$router.push({path: '/index/' + path, query: {detailObj: JSON.stringify(item)}});
		},
		moreBtn(path) {
			this.$router.push({path: '/index/' + path});
		}
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
	
		.recommend {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
        }
        
        .list5 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform:  translate3d(0px, -10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: kew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
		
		.news {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list6 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list6 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform:  translate3d(10px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform:  skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	
		.lists {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
        }
        
        .list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-next {
            left: auto;
            right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform:  skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
		}
	}
</style>
