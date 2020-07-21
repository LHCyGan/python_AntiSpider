!function(e) {
    "function" == typeof define && define.amd ? define(e) : e()
}(function() {
    "use strict";
    var o = !1;
    var a = {
        getCookies: function() {
            var t = {};
            try {
                for (var e = document.cookie ? document.cookie.split("; ") : [], r = 0; r < e.length; r++) {
                    var n = e[r].split("=");
                    t[n[0]] = decodeURIComponent(n[1])
                }
                return t
            } catch (e) {
                return console.error("获取 cookies 失败", e),
                window.zpStat && window.zpStat.error && window.zpStat.error(e, "获取 cookies 失败"),
                t
            }
        },
        getCurrentUrlPath: function(e) {
            var t = "";
            return "string" == typeof e && (t = e.replace(/^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/, "$3/$5")),
            t
        },
        copyMembers: function(e, t) {
            if (t)
                for (var r in t)
                    t.hasOwnProperty(r) && (e[r] = t[r])
        },
        addEventListener: function(e, t, r) {
            e.addEventListener ? e.addEventListener(t, r, !1) : e.attachEvent("on".concat(t), r)
        },
        removeEventListener: function(e, t, r) {
            e.removeEventListener ? e.removeEventListener(t, r) : e.detachEvent("on".concat(t), r)
        }
    }
      , r = a.getCurrentUrlPath
      , i = [".zhaopin.com", ".zhaopin.cn", ".highpin.cn"];
    var n = {
        get: function(e) {
            var t = "; ".concat(document.cookie).split("; ".concat(e, "="));
            return 2 === t.length ? t.pop().split(";").shift() : null
        },
        set: function(e, t, r) {
            for (var n = null, o = 0; o < i.length; o++)
                RegExp("".concat(i[o], "$")).test(window.location.hostname) && (n = i[o]);
            n || console.warn("当前域名不在白名单内，白名单列表：".concat(i.join(", ")));
            var a = new Date;
            a.setTime(a.getTime() + 24 * r * 60 * 60 * 1e3),
            document.cookie = "".concat(e, "=").concat(t, "; expires=").concat(a.toUTCString(), "; domain=").concat(n, "; path=/")
        }
    }
      , c = {
        generate: function() {
            var r = (new Date).getTime();
            return void 0 !== window.performance && "function" == typeof window.performance.now && (r += window.performance.now()),
            "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                var t = (r + 16 * Math.random()) % 16 | 0;
                return ("x" === e ? t : 7 & t | 8).toString(16)
            })
        }
    };
    var s = {
        get: function() {
            var e, t = "";
            try {
                (e = n.get("x-zp-client-id")) || (e = c.generate(),
                n.set("x-zp-client-id", e, 36500)),
                t = e
            } catch (e) {
                console.error(e.message)
            }
            return t
        }
    };
    var p, u = {
        get: function() {
            var e = {}
              , t = window.zpPageRequestId;
            t && (e["x-zp-page-request-id"] = t);
            var r = s.get();
            return r && (e["x-zp-client-id"] = r),
            e
        }
    };
    var e = {
        get: function() {
            var e = window.zpStatConfig || {}
              , t = {};
            a.copyMembers(t, e.page || {}),
            e.isSPA && (t.isSPA = !0);
            var r = u.get();
            for (var n in r)
                r.hasOwnProperty(n) && (t[n.replace(/-/g, "_")] = r[n]);
            t.current_url = document.location.href,
            t.current_url_path = a.getCurrentUrlPath(document.location.href),
            t.referrer = t.isSPA && p ? p.current_url : document.referrer;
            var o = a.getCookies();
            return o.at && o.rt && (t.passport_at = o.at,
            t.passport_rt = o.rt),
            p = t
        }
    };
    var d = {
        get: function() {
            var e = window.zpStatConfig && (window.zpStatConfig.sa || {})
              , t = {};
            return a.copyMembers(t, e),
            t
        }
    }
      , l = e.get()
      , w = "sa";
    function f(e) {
        try {
            var t = e.getAttribute("zp-stat-id");
            if (!t)
                return {};
            for (var r = {
                stat_id: t
            }, n = e.attributes, o = 0; o < n.length; o++) {
                var a = n[o].name;
                "zp-stat-id" !== a && (0 == a.indexOf("zp-stat-") && (r[a = a.substr(8).replace(/-/g, "_")] = n[o].value))
            }
            return r.track && window.zpStat && window.zpStat.track && window.zpStat.track(r.track, r),
            r
        } catch (e) {
            return window.zpStat && window.zpStat.error && window.zpStat.error(e.message, "提取自定义上报信息失败"),
            {}
        }
    }
    function g(e) {
        return window.sa && window.sa[e]
    }
    !function(e) {
        try {
            var t = e.sdk_url
              , r = e.name
              , n = window
              , o = document
              , a = null
              , i = null;
            n.sensorsDataAnalytic201505 = r,
            n[r] = n[r] || function(e) {
                return function() {
                    (n[r]._q = n[r]._q || []).push([e, arguments])
                }
            }
            ;
            for (var c = ["track", "quick", "register", "registerPage", "registerOnce", "trackSignup", "trackAbtest", "setProfile", "setOnceProfile", "appendProfile", "incrementProfile", "deleteProfile", "unsetProfile", "identify", "login", "logout", "trackLink", "clearAllRegister", "getAppStatus"], s = 0; s < c.length; s++)
                n[r][c[s]] = n[r].call(null, c[s]);
            n[r]._t || (a = o.createElement("script"),
            i = o.getElementsByTagName("script")[0],
            a.async = 1,
            a.src = t,
            a.setAttribute("charset", "UTF-8"),
            i.parentNode.insertBefore(a, i),
            n[r].para = e)
        } catch (e) {
            console.error("神策SDK默认初始化错误", e)
        }
    }(function() {
        var e = function() {
            var e = {
                A1: "zlbusiness",
                A: "zlclient",
                B: "highpin",
                E1: "zlcrm",
                E: "itoa",
                F: "production",
                G14: "zlclient",
                G: "production",
                H: "zlclient",
                J: "zlbschool",
                K: "hremail",
                L: "talentdev"
            }
              , t = l.appid;
            if (o || !t)
                return "default";
            var r = t.substr(0, 2)
              , n = t.substr(0, 1);
            return e[t] ? e[t] : e[r] ? e[r] : e[n] ? e[n] : "default"
        }()
          , t = {
            sdk_url: "https://statistic.zhaopin.cn/sdk/sa/1.14.11/sa.min.js",
            heatmap_url: "https://statistic.zhaopin.cn/sdk/sa/1.14.11/heap_map.min.js",
            name: w,
            show_log: !!o,
            web_url: "https://dsm.zhaopin.cn/?project=".concat(e),
            server_url: "https://ds.zhaopin.cn/sa?project=".concat(e),
            heatmap: {
                custom_property: f
            }
        };
        a.copyMembers(t, d.get());
        try {
            void 0 !== window.localStorage && void 0 !== window.localStorage.zpfe_stat_sa_show_log && (t.show_log = "true" === window.localStorage.getItem("zpfe_stat_sa_show_log"))
        } catch (e) {}
        return t
    }()),
    window[w].registerPage && window[w].registerPage(l),
    !0 !== l.isSPA && window[w].quick && window[w].quick("autoTrack"),
    window.zpStat = {
        track: function(e, t, r) {
            g("track") && window.sa.track(e, t, r)
        },
        login: function(e) {
            g("login") && window.sa.login(e)
        },
        logout: function(e) {
            g("logout") && window.sa.logout(e)
        },
        setProfile: function(e, t) {
            g("setProfile") && window.sa.setProfile(e, t)
        },
        error: function(e, t) {
            e && (console.error(t, e),
            g("track") && window.sa.track("zp_ui_error", {
                zp_ui_error_message: e.message,
                zp_ui_error_stack: e.stack,
                zp_ui_error_description: t,
                current_url_path: r(document.location.href)
            }))
        },
        refreshPageConfig: function() {
            g("track") && window.sa.registerPage(e.get())
        },
        switchPage: function() {
            var e = this;
            g("quick") && setTimeout(function() {
                e.refreshPageConfig(),
                window.sa.quick("autoTrackSinglePage")
            }, 100)
        }
    };
    var m = {
        get: function() {
            var e = window.zpStatConfig
              , t = {
                params: {},
                ignore: null
            };
            return a.copyMembers(t.params, u.get()),
            e && e.passThrough && Array.isArray(e.passThrough.ignore) && e.passThrough.ignore.length && (t.ignore = e.passThrough.ignore),
            t
        }
    };
    !function() {
        var e = window.XMLHttpRequest;
        if (e) {
            var s = e.prototype.open;
            e.prototype.open = function() {
                for (var e = arguments.length, t = Array(e), r = 0; r < e; r++)
                    t[r] = arguments[r];
                var n = t[1]
                  , o = n;
                if (!function(e) {
                    var t = !1
                      , r = m.get().ignore;
                    if (!r)
                        return t;
                    for (var n = 0; n < r.length; n++)
                        r[n].test(e) && (t = !0);
                    return t
                }(n)) {
                    var a = m.get().params;
                    for (var i in a) {
                        var c = -1 < o.indexOf("?") ? "&" : "?";
                        o += "".concat(c).concat(i, "=").concat(a[i])
                    }
                }
                t[1] = o,
                s.apply(this, t)
            }
        }
    }(),
    a.addEventListener(window, "error", function(e) {
        var t;
        (t = e).error && t.error.stack && -1 != t.error.stack.indexOf(".zhaopin.c") && (window.zpStat && window.zpStat.error ? window.zpStat.error(e.error, "发现未捕获的错误") : console.error("发现未捕获的错误", e.error))
    });
    var t, h, v = 3e4;
    function _(e, t) {
        var r = Math.abs(parseInt(t - e));
        return v < r && (r = 0),
        r
    }
    function z(e) {
        return decodeURIComponent(window.location.search.replace(RegExp("^(?:.*[&\\?]".concat(encodeURIComponent(e).replace(/[.+*]/g, "\\$&"), "(?:\\=([^&]*))?)?.*$"), "i"), "$1"))
    }
    a.addEventListener(window, "load", function() {
        var e = function() {
            if (!window.performance || !window.performance.timing)
                return null;
            var e = window.performance.timing
              , t = _(e.redirectStart, e.redirectEnd)
              , r = _(e.domainLookupStart, e.domainLookupEnd)
              , n = _(e.connectStart, e.connectEnd)
              , o = _(e.requestStart, e.responseStart)
              , a = _(e.responseStart, e.responseEnd)
              , i = _(e.domLoading, e.domInteractive)
              , c = _(e.domInteractive, e.domComplete)
              , s = _(e.navigationStart, e.domComplete);
            return {
                zp_performance_redirect: t,
                zp_performance_domain_lookup: r,
                zp_performance_tcp: n,
                zp_performance_request: o,
                zp_performance_response: a,
                zp_performance_dom_content_load: i,
                zp_performance_dom_processing: c,
                zp_performance_dom_complete: s
            }
        }();
        e && window.zpStat.track("zp_ui_performance", e)
    }),
    t = z("chuda_user_id"),
    h = z("exp_id"),
    t && (window.zpStat.login(t),
    window.zpStat.track("chuda_pageopen", {
        exp_id: h
    }))
});
