"use strict";function debuglog(e){if(void 0===debugEnviron&&(debugEnviron=process.env.NODE_DEBUG||""),e=e.toUpperCase(),!debugs[e])if(new RegExp("\\b"+e+"\\b","i").test(debugEnviron)){var u=process.pid;debugs[e]=function(){var r=util.format.apply(util,arguments);console.error("%s %d: %s",e,u,r)}}else debugs[e]=function(){};return debugs[e]}var debugs={},debugEnviron,util=require("util");module.exports=debuglog;