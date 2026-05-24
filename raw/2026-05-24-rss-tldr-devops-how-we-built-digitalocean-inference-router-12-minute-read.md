---
source: "https://www.digitalocean.com/blog/inference-router-architecture"
title: "How We Built DigitalOcean Inference Router (12 minute read)"
author: "TLDR DevOps"
date_published: "Fri, 22 May 2026 00:00:00 GMT"
date_clipped: "2026-05-24"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-05-22"
source_role: "primary-via-tldr"
---

# How We Built DigitalOcean Inference Router (12 minute read)

Source: https://www.digitalocean.com/blog/inference-router-architecture

How We Built DigitalOcean Inference Router | DigitalOcean .cuqQyD{text-decoration:none;}/*!sc*/
.cuqQyD.button-link{align-items:center;background-color:transparent;border:1px solid #080b2d;border-radius:100px;color:#080b2d;cursor:pointer;display:flex;font-size:1em;font-weight:700;justify-content:center;padding:16px 32px;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link:hover{background-color:rgba(0,105,255,0.15);color:#080b2d;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link:focus{background-color:rgba(0,105,255,0.15);border:1px solid transparent;color:#0069ff;}/*!sc*/
.cuqQyD.button-link.is-squared{border-radius:8px;}/*!sc*/
.cuqQyD.button-link.is-primary{background-color:#1633ff;border:1px solid #1633ff;color:#fff;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-primary:hover{background-color:#0069ff;border:1px solid #0069ff;color:#fff!important;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-primary:disabled{background-color:#c4c9d6!important;border:1px solid #c4c9d6!important;color:#fff;}/*!sc*/
.cuqQyD.button-link.is-primary.is-outlined{border:1px solid #0069ff;color:#0069ff;}/*!sc*/
.cuqQyD.button-link.is-primary.is-outlined:hover{background-color:rgba(0,105,255,0.1);border:1px solid #0069ff!important;color:#0069ff!important;}/*!sc*/
.cuqQyD.button-link.is-primary.is-outlined:disabled{background-color:#fff!important;border:1px solid #8690a9!important;color:#8690a9!important;}/*!sc*/
.cuqQyD.button-link.is-white{background-color:#fff;border:1px solid #fff;color:#0069ff;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-white:hover{background-color:rgba(225,225,225,0.9);border:1px solid rgba(225,225,225,0.9);color:#0069ff!important;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-white:disabled{border:1px solid #8690a9!important;color:#8690a9!important;}/*!sc*/
.cuqQyD.button-link.is-white.is-outlined{background-color:transparent;border:1px solid rgba(255,255,255,0.8);color:rgba(255,255,255,0.8);}/*!sc*/
.cuqQyD.button-link.is-white.is-outlined:hover{background-color:transparent;border:1px solid rgba(255,255,255,1);color:rgba(255,255,255,1)!important;}/*!sc*/
.cuqQyD.button-link.is-green{background-color:#15CD72;border:1px solid #15CD72;color:#fff;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-green:hover{background-color:rgba(21, 205, 114, 0.9);border:1px solid rgba(21, 205, 114, 0.9);color:#fff!important;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-green:disabled{border:1px solid rgba(21, 205, 114, 0.3)!important;color:rgba(21, 205, 114, 0.3)!important;}/*!sc*/
.cuqQyD.button-link.is-green.is-outlined{background-color:transparent;border:1px solid rgba(21, 205, 114, 0.9);color:rgba(21, 205, 114, 0.9);}/*!sc*/
.cuqQyD.button-link.is-green.is-outlined:not(:disabled):hover{background-color:transparent;border:1px solid rgba(21, 205, 114, 1);color:rgba(21, 205, 114, 1);}/*!sc*/
.cuqQyD.button-link.is-outlined{background-color:transparent;border:1px solid #080b2d;color:#080b2d;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-outlined:hover{border:1px solid #0069ff;color:#0069ff;transition:all 0.3s ease;}/*!sc*/
.cuqQyD.button-link.is-small{padding:12px 24px;}/*!sc*/
.cuqQyD.button-link.has-center-img{padding:15px 16px;}/*!sc*/
.cuqQyD.button-link.has-left-img >img{margin-right:8px;}/*!sc*/
.cuqQyD.button-link.mx-16{margin-left:16px;margin-right:16px;}/*!sc*/
.cuqQyD.button-link.is-gray3-color{box-shadow:0 6px 20px -6px rgba(11, 43, 158, 0.15);color:#24335a;font-size:16px;font-weight:600;line-height:24px;}/*!sc*/
data-styled.g1[id="LazyLink___StyledLink-sc-a535d946-0"]{content:"cuqQyD,"}/*!sc*/
.geOKRH{text-decoration:none;}/*!sc*/
.geOKRH.button-link{align-items:center;background-color:transparent;border:1px solid #080b2d;border-radius:100px;color:#080b2d;cursor:pointer;display:flex;font-size:1em;font-weight:700;justify-content:center;padding:16px 32px;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link:hover{background-color:rgba(0,105,255,0.15);color:#080b2d;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link:focus{background-color:rgba(0,105,255,0.15);border:1px solid transparent;color:#0069ff;}/*!sc*/
.geOKRH.button-link.is-squared{border-radius:8px;}/*!sc*/
.geOKRH.button-link.is-primary{background-color:#1633ff;border:1px solid #1633ff;color:#fff;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-primary:hover{background-color:#0069ff;border:1px solid #0069ff;color:#fff!important;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-primary:disabled{background-color:#c4c9d6!important;border:1px solid #c4c9d6!important;color:#fff;}/*!sc*/
.geOKRH.button-link.is-primary.is-outlined{border:1px solid #0069ff;color:#0069ff;}/*!sc*/
.geOKRH.button-link.is-primary.is-outlined:hover{background-color:rgba(0,105,255,0.1);border:1px solid #0069ff!important;color:#0069ff!important;}/*!sc*/
.geOKRH.button-link.is-primary.is-outlined:disabled{background-color:#fff!important;border:1px solid #8690a9!important;color:#8690a9!important;}/*!sc*/
.geOKRH.button-link.is-white{background-color:#fff;border:1px solid #fff;color:#0069ff;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-white:hover{background-color:rgba(225,225,225,0.9);border:1px solid rgba(225,225,225,0.9);color:#0069ff!important;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-white:disabled{border:1px solid #8690a9!important;color:#8690a9!important;}/*!sc*/
.geOKRH.button-link.is-white.is-outlined{background-color:transparent;border:1px solid rgba(255,255,255,0.8);color:rgba(255,255,255,0.8);}/*!sc*/
.geOKRH.button-link.is-white.is-outlined:hover{background-color:transparent;border:1px solid rgba(255,255,255,1);color:rgba(255,255,255,1)!important;}/*!sc*/
.geOKRH.button-link.is-green{background-color:#15CD72;border:1px solid #15CD72;color:#fff;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-green:hover{background-color:rgba(21, 205, 114, 0.9);border:1px solid rgba(21, 205, 114, 0.9);color:#fff!important;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-green:disabled{border:1px solid rgba(21, 205, 114, 0.3)!important;color:rgba(21, 205, 114, 0.3)!important;}/*!sc*/
.geOKRH.button-link.is-green.is-outlined{background-color:transparent;border:1px solid rgba(21, 205, 114, 0.9);color:rgba(21, 205, 114, 0.9);}/*!sc*/
.geOKRH.button-link.is-green.is-outlined:not(:disabled):hover{background-color:transparent;border:1px solid rgba(21, 205, 114, 1);color:rgba(21, 205, 114, 1);}/*!sc*/
.geOKRH.button-link.is-outlined{background-color:transparent;border:1px solid #080b2d;color:#080b2d;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-outlined:hover{border:1px solid #0069ff;color:#0069ff;transition:all 0.3s ease;}/*!sc*/
.geOKRH.button-link.is-small{padding:12px 24px;}/*!sc*/
.geOKRH.button-link.has-center-img{padding:15px 16px;}/*!sc*/
.geOKRH.button-link.has-left-img >img{margin-right:8px;}/*!sc*/
.geOKRH.button-link.mx-16{margin-left:16px;margin-right:16px;}/*!sc*/
.geOKRH.button-link.is-gray3-color{box-shadow:0 6px 20px -6px rgba(11, 43, 158, 0.15);color:#24335a;font-size:16px;font-weight:600;line-height:24px;}/*!sc*/
data-styled.g2[id="LazyLink___StyledA-sc-a535d946-1"]{content:"geOKRH,"}/*!sc*/
.cAziLP{bottom:40px;display:flex;flex-direction:column;gap:4px;left:24px;max-width:calc(100% - 48px);position:fixed;z-index:99999;}/*!sc*/
.cAziLP svg{align-self:flex-start;margin-top:4px;}/*!sc*/
@media (min-width:768px){.cAziLP{left:40px;}}/*!sc*/
@media (min-width:1280px){.cAziLP{left:64px;}}/*!sc*/
data-styled.g19[id="NotificationsStyles__NotificationsContainer-sc-69d0afda-0"]{content:"cAziLP,"}/*!sc*/
.gjcknJ{margin:0;color:var(--text-on-color);font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:500;}/*!sc*/
.dgkEct{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:400;border:0;clip:rect(0 0 0 0);clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px;}/*!sc*/
.dtGlsG{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:500;}/*!sc*/
.hyCPry{margin:0;color:var(--text-primary);font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:500;}/*!sc*/
.dbZMJb{margin:0;color:var(--text-default);font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:500;}/*!sc*/
.bwDPig{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:18px;letter-spacing:0;line-height:26px;font-weight:700;}/*!sc*/
.lpcyAX{margin:0;color:var(--text-default);font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:700;}/*!sc*/
.gtmsSS{margin:0;color:var(--text-default);font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:400;}/*!sc*/
.crBLPr{margin:0;color:var(--text-default);font-family:'Inter','Inter Fallback',sans-serif;font-size:18px;letter-spacing:0;line-height:26px;font-weight:700;}/*!sc*/
.eOTlCl{margin:0;color:var(--text-on-color);font-family:'Inter','Inter Fallback',sans-serif;font-size:12px;letter-spacing:0;line-height:18px;font-weight:400;}/*!sc*/
.iokouU{margin:0;color:var(--text-primary);font-family:'Plus Jakarta Sans',sans-serif;font-size:28px;letter-spacing:0;line-height:36px;font-weight:700;}/*!sc*/
@media (min-width: 768px){.iokouU{font-size:48px;letter-spacing:-1.5px;line-height:56px;}}/*!sc*/
.iCwRz{margin:0;color:#4D5B7C;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:400;}/*!sc*/
.dzPdbq{margin:0;color:#4D5B7C;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:500;}/*!sc*/
.fUTSys{margin:0;color:#4D5B7C;font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:500;}/*!sc*/
.bPyayz{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:400;}/*!sc*/
.dilltD{margin:0;color:#000C2A;font-family:'Inter','Inter Fallback',sans-serif;font-size:18px;letter-spacing:0;line-height:26px;font-weight:700;}/*!sc*/
.pVJDr{margin:0;color:#000C2A;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:700;}/*!sc*/
.eqLHEl{margin:0;color:#4D5B7C;font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:400;}/*!sc*/
.enjFhe{margin:0;color:#000C2A;font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:400;}/*!sc*/
.bUdUxy{margin:0;color:#000C2A;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:600;}/*!sc*/
.ffgMnF{margin:0;color:var(--text-primary);font-family:'Plus Jakarta Sans',sans-serif;font-size:28px;letter-spacing:0;line-height:36px;font-weight:700;}/*!sc*/
@media (min-width: 768px){.ffgMnF{font-size:36px;letter-spacing:-1px;line-height:48px;}}/*!sc*/
.juyKFJ{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;letter-spacing:0;line-height:32px;font-weight:700;}/*!sc*/
.fSNOKV{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:400;}/*!sc*/
.jkauUM{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:14px;letter-spacing:0;line-height:20px;font-weight:500;}/*!sc*/
.dmpoCR{margin:0;font-family:'Inter','Inter Fallback',sans-serif;font-size:16px;letter-spacing:0;line-height:24px;font-weight:600;}/*!sc*/
data-styled.g24[id="Typographystyles-sc-o7qsl9-0"]{content:"gjcknJ,dgkEct,dtGlsG,hyCPry,dbZMJb,bwDPig,lpcyAX,gtmsSS,crBLPr,eOTlCl,iokouU,iCwRz,dzPdbq,fUTSys,bPyayz,dilltD,pVJDr,eqLHEl,enjFhe,bUdUxy,ffgMnF,juyKFJ,fSNOKV,jkauUM,dmpoCR,"}/*!sc*/
.IuizA{align-items:center;background-color:#001515;border:1px solid var(--border-transparent);border-radius:9999px;bottom:24px;display:flex;gap:8px;justify-content:center;padding:8px 16px;position:fixed;right:24px;transition:gap 0.3s ease,padding 0.3s ease;z-index:100;}/*!sc*/
.IuizA:hover{gap:8px;padding:8px 16px;}/*!sc*/
data-styled.g25[id="DarkModeChipStyles__StyledDarkModeChip-sc-191a31af-0"]{content:"IuizA,"}/*!sc*/
.gBdVqa{display:inline-flex;max-width:240px;opacity:1;overflow:hidden;transition:max-width 0.3s ease,opacity 0.3s ease;white-space:nowrap;}/*!sc*/
.DarkModeChipStyles__StyledDarkModeChip-sc-191a31af-0:hover .gBdVqa{max-width:240px;opacity:1;}/*!sc*/
data-styled.g26[id="DarkModeChipStyles__ChipLabel-sc-191a31af-1"]{content:"gBdVqa,"}/*!sc*/
.ePCZnM{display:grid;gap:24px;grid-template-columns:repeat(6,minmax(0,1fr));}/*!sc*/
@media (min-width: 768px){.ePCZnM{gap:24px;}}/*!sc*/
.hQbALw{display:grid;gap:24px;grid-template-columns:repeat(1,minmax(0,1fr));}/*!sc*/
@media (min-width: 768px){.hQbALw{gap:32px;}}/*!sc*/
.ePCZrz{display:grid;gap:24px;grid-template-columns:repeat(6,minmax(0,1fr));}/*!sc*/
@media (min-width: 768px){.ePCZrz{gap:32px;}}/*!sc*/
data-styled.g27[id="Gridstyles-sc-isu2n3-0"]{content:"ePCZnM,hQbALw,ePCZrz,"}/*!sc*/
.hdrwgM{grid-column:span 1;}/*!sc*/
.dryhdA{grid-column:span 6;}/*!sc*/
@media (min-width: 768px){.dryhdA{grid-column:span 3;}}/*!sc*/
@media (min-width: 1024px){.dryhdA{grid-column:span 2;}}/*!sc*/
data-styled.g40[id="GridItemstyles-sc-eu71zi-0"]{content:"hdrwgM,dryhdA,"}/*!sc*/
.jznjUW{background:linear-gradient( var(--text-accent),var(--text-accent) ) bottom repeat-x;background-size:1px 1px;color:var(--text-accent);position:relative;text-decoration:none;transition:background 300ms ease-in-out,color 300ms ease-in-out;}/*!sc*/
.jznjUW:hover,.jznjUW:focus{background-size:100% 100%;color:var(--text-on-color);}/*!sc*/
data-styled.g41[id="LinkInlinestyles-sc-18du0ds-0"]{content:"jznjUW,"}/*!sc*/
.lhAqRU{cursor:pointer;display:inline-block;font-weight:600;border-radius:32px;font-size:16px;line-height:24px;padding:8px 24px;background-color:transparent;box-shadow:inset 0px 0px 0px 1px var(--button-ghost-default);color:var(--button-ghost-default);transition:background 300ms ease-in-out,color 300ms ease-in-out;}/*!sc*/
.lhAqRU:hover{box-shadow:none;background-color:var(--button-ghost-hover);color:var(--button-white-text);}/*!sc*/
.lhAqRU:focus-visible{box-shadow:none;background-color:var(--button-ghost-hover);color:var(--button-white-text);outline-color:var(--button-ghost-hover);}/*!sc*/
.lhAqRU:focus-visible{outline-offset:2px;outline-style:solid;outline-width:2px;}/*!sc*/
.gZqenS{cursor:pointer;display:inline-block;font-weight:600;border-radius:32px;font-size:16px;line-height:24px;padding:8px 24px;background-color:transparent;color:var(--text-default);font-weight:500;padding:8px 16px;transition:color 300ms ease-in-out,background-color 300ms ease-in-out;}/*!sc*/
.gZqenS:hover{background-color:var(--navigation-www-nav-card-hover);color:var(--text-primary);}/*!sc*/
.gZqenS:focus-visible{background-color:var(--navigation-www-nav-card-hover);color:var(--text-primary);outline-color:var(--navigation-www-nav-card-hover);}/*!sc*/
.gZqenS:focus-visible{outline-offset:2px;outline-style:solid;outline-width:2px;}/*!sc*/
.hNUIgQ{cursor:pointer;display:inline-block;font-weight:600;border-radius:32px;font-size:16px;line-height:24px;padding:8px 24px;background-color:var(--button-primary-default);color:var(--button-primary-text);font-weight:500;padding:8px 16px;transition:background 300ms ease-in-out;}/*!sc*/
.hNUIgQ:hover{background-color:var(--button-primary-hover);}/*!sc*/
.hNUIgQ:focus-visible{background-color:var(--button-primary-hover);outline-color:var(--button-primary-hover);}/*!sc*/
.hNUIgQ:focus-visible{outline-offset:2px;outline-style:solid;outline-width:2px;}/*!sc*/
.dPHdBa{cursor:pointer;display:inline-block;font-weight:600;border-radius:40px;font-size:14px;line-height:20px;padding:6px 16px;background-color:transparent;box-shadow:inset 0px 0px 0px 1px var(--button-ghost-default);color:var(--button-ghost-default);transition:background 300ms ease-in-out,color 300ms ease-in-out;}/*!sc*/
.dPHdBa:hover{box-shadow:none;background-color:var(--button-ghost-hover);color:var(--button-white-text);}/*!sc*/
.dPHdBa:focus-visible{box-shadow:none;background-color:var(--button-ghost-hover);color:var(--button-white-text);outline-color:var(--button-ghost-hover);}/*!sc*/
.dPHdBa:focus-visible{outline-offset:2px;outline-style:solid;outline-width:2px;}/*!sc*/
data-styled.g44[id="Buttonstyles-sc-hznqte-1"]{content:"lhAqRU,gZqenS,hNUIgQ,dPHdBa,"}/*!sc*/
.eAyde{align-items:center;background-color:#B5F6FF;border-radius:999px;color:var(--text-primary);display:flex;font-weight:500;justify-content:center;width:100%;padding:6px 16px;font-size:12px;line-height:18px;letter-spacing:0;}/*!sc*/
data-styled.g47[id="ProductCardTagstyles__StyledProductCardTag-sc-1qe54hc-0"]{content:"eAyde,"}/*!sc*/
.kJsCek{color:var(--text-always-dark);display:inline-block;font-weight:600;line-height:0;width:fit-content;}/*!sc*/
.kJsCek span,.kJsCek a{border-radius:8px;font-size:16px;line-height:24px;padding:8px 16px;background-color:#8AABFF;align-items:center;display:inline-flex;gap:2px;overflow:hidden;}/*!sc*/
.kJsCek span >svg,.kJsCek a >svg{flex-shrink:0;}/*!sc*/
.kJsCek a{display:block;position:relative;transition:background-color 300ms ease-in-out;}/*!sc*/
.kJsCek a:hover{background-color:#8AABFF;}/*!sc*/
.kJsCek a:focus-visible{outline:2px solid #8AABFF;outline-width:2px;}/*!sc*/
.ckqcrI{color:#000C2A;display:inline-block;font-weight:600;line-height:0;width:fit-content;}/*!sc*/
.ckqcrI span,.ckqcrI a{border-radius:6px;font-size:14px;line-height:20px;padding:4px 8px;background-color:#8AABFF;align-items:center;display:inline-flex;gap:2px;overflow:hidden;}/*!sc*/
.ckqcrI span >svg,.ckqcrI a >svg{flex-shrink:0;}/*!sc*/
.ckqcrI a{display:block;position:relative;transition:background-color 300ms ease-in-out;}/*!sc*/
.ckqcrI a:hover{background-color:#8AABFF;}/*!sc*/
.ckqcrI a:focus-visible{outline:2px solid #8AABFF;outline-width:2px;}/*!sc*/
data-styled.g52[id="Categorystyles__StyledCategory-sc-1lstx5-0"]{content:"kJsCek,ckqcrI,"}/*!sc*/
.cqgzyr{align-items:center;display:inline-flex;gap:8px;line-height:1.5;position:relative;text-decoration:none;}/*!sc*/
.cqgzyr::after{background:currentColor;bottom:2px;content:'';height:1.5px;left:0;position:absolute;transform:scaleX(0);transform-origin:0 0;transition:transform 300ms ease-in-out;width:100%;}/*!sc*/
.cqgzyr path{transition:transform 300ms ease-in-out;}/*!sc*/
.cqgzyr path:nth-child(1){transform:translateX(-5px);}/*!sc*/
.cqgzyr path:nth-child(2){transform:scaleX(0.6333333333);transform-origin:0 0;}/*!sc*/
.cqgzyr:hover::after,.cqgzyr:focus::after{transform:scaleX(1);}/*!sc*/
.cqgzyr:hover path:nth-child(1),.cqgzyr:focus path:nth-child(1){transform:translateX(0);}/*!sc*/
.cqgzyr:hover path:nth-child(2),.cqgzyr:focus path:nth-child(2){transform:scaleX(1);}/*!sc*/
.cqgzyr svg{flex-shrink:0;height:12px;width:18px;}/*!sc*/
data-styled.g53[id="LinkTextstyles-sc-jz3jcd-0"]{content:"cqgzyr,"}/*!sc*/
.jcrsPx{border-radius:16px;overflow:hidden;position:relative;}/*!sc*/
.jcrsPx::after{content:'';display:block;padding-bottom:58.08823529411765%;}/*!sc*/
@media (min-width: 768px){.jcrsPx::after{padding-bottom:57.89473684210527%;}}/*!sc*/
.jcrsPx img{height:100%;inset:0;object-fit:cover;position:absolute;width:100%;}/*!sc*/
data-styled.g55[id="CardUniversalstyles__StyledCardUniversalImage-sc-1inzdla-1"]{content:"jcrsPx,"}/*!sc*/
.bLaCJy{display:flex;flex-direction:column;gap:24px;justify-content:space-between;}/*!sc*/
data-styled.g56[id="CardUniversalstyles__StyledCardUniversalContainer-sc-1inzdla-2"]{content:"bLaCJy,"}/*!sc*/
.dgnWJE{display:flex;flex-direction:column;gap:16px;}/*!sc*/
data-styled.g57[id="CardUniversalstyles__StyledCardUniversalContent-sc-1inzdla-3"]{content:"dgnWJE,"}/*!sc*/
.whhtC{display:flex;flex-direction:column;gap:8px;}/*!sc*/
data-styled.g59[id="CardUniversalstyles__StyledCardUniversalMainContent-sc-1inzdla-5"]{content:"whhtC,"}/*!sc*/
.kMeHEC{position:relative;}/*!sc*/
data-styled.g60[id="CardUniversalstyles__StyledCardUniversalLink-sc-1inzdla-6"]{content:"kMeHEC,"}/*!sc*/
.iwxXGF{align-items:center;display:flex;gap:16px;}/*!sc*/
.iwxXGF svg{color:var(--icon-brand);}/*!sc*/
.iwxXGF a{transition:color 300ms ease-in-out;}/*!sc*/
.iwxXGF a:hover{color:var(--icon-brand);}/*!sc*/
data-styled.g61[id="CardUniversalstyles__StyledCardUniversalHeader-sc-1inzdla-7"]{content:"iwxXGF,"}/*!sc*/
.hAucvG{display:flex;flex-direction:column;min-height:100%;color:var(--text-primary);background-color:var(--background-card);border-radius:16px;overflow:hidden;position:relative;}/*!sc*/
.hAucvG::after{border:2px solid var(--border-transparent);border-radius:16px;content:'';inset:0;pointer-events:none;position:absolute;}/*!sc*/
.hAucvG .CardUniversalstyles__StyledCardUniversalContainer-sc-1inzdla-2{flex-grow:1;padding:32px 32px 40px;}/*!sc*/
.hAucvG .CardUniversalstyles__StyledCardUniversalImage-sc-1inzdla-1{border-radius:0;}/*!sc*/
.hAucvG .CardUniversalstyles__StyledCardUniversalImage-sc-1inzdla-1 +.CardUniversalstyles__StyledCardUniversalContainer-sc-1inzdla-2{padding:24px 32px 40px;}/*!sc*/
.hAucvG .CardUniversalstyles__StyledCardUniversalLink-sc-1inzdla-6{margin-top:auto;}/*!sc*/
.hAucvG +:not(.CardUniversalstyles__StyledCardUniversalLink-sc-1inzdla-6) .CardUniversalstyles__StyledCardUniversalFooter-sc-1inzdla-0{margin-top:auto;}/*!sc*/
data-styled.g64[id="CardUniversalstyles__StyledCardUniversal-sc-1inzdla-10"]{content:"hAucvG,"}/*!sc*/
.gXgzEv{overflow-wrap:break-word;}/*!sc*/
.gXgzEv a{color:var(--links-author-default);text-decoration:underline;}/*!sc*/
.gXgzEv a:hover{color:var(--links-author-hover);text-decoration:none;}/*!sc*/
data-styled.g65[id="CardUniversalstyles__StyledAuthor-sc-1inzdla-11"]{content:"gXgzEv,"}/*!sc*/
.dTonFi{display:flex;flex-direction:column;gap:4px;}/*!sc*/
data-styled.g66[id="CardUniversalstyles__StyledMetaData-sc-1inzdla-12"]{content:"dTonFi,"}/*!sc*/
.bGgPlx{display:flex;flex-wrap:wrap;gap:4px 8px;list-style-type:none;padding:0;}/*!sc*/
.bGgPlx >li{align-items:center;color:#4D5B7C;display:flex;gap:8px;}/*!sc*/
.bGgPlx >li svg,.bGgPlx >li img{height:16px;width:16px;}/*!sc*/
.bGgPlx >li::after{content:'•';}/*!sc*/
.bGgPlx >li:last-child::after{display:none;}/*!sc*/
data-styled.g67[id="CardUniversalstyles__StyledMetaInfo-sc-1inzdla-13"]{content:"bGgPlx,"}/*!sc*/
.jwTpaH{isolation:isolate;position:relative;}/*!sc*/
data-styled.g69[id="Sectionstyles__StyledSection-sc-4l5hhw-0"]{content:"jwTpaH,"}/*!sc*/
.bMHhFg{--k-padding:72px;background-color:var(--background-accent);padding:var(--k-padding) 0;}/*!sc*/
@media (min-width: 768px){.bMHhFg{--k-padding:96px;}}/*!sc*/
.halAfQ{--k-padding:72px;padding:var(--k-padding) 0;}/*!sc*/
@media (min-width: 768px){.halAfQ{--k-padding:72px;}}/*!sc*/
.heagBN{--k-padding:72px;background-color:#F9FAFE;padding:var(--k-padding) 0;}/*!sc*/
@media (min-width: 768px){.heagBN{--k-padding:96px;}}/*!sc*/
data-styled.g70[id="Sectionstyles__StyledSectionInner-sc-4l5hhw-1"]{content:"bMHhFg,halAfQ,heagBN,"}/*!sc*/
.dufmut{--k-container-padding:24px;--k-container-max-width:1088px;margin:0 auto;max-width:calc( var(--k-container-max-width) + calc(var(--k-container-padding) * 2) );padding:0 var(--k-container-padding);width:100%;}/*!sc*/
@media (min-width: 768px){.dufmut{--k-container-padding:40px;}}/*!sc*/
.ivbozM{--k-container-padding:0px;--k-container-max-width:864px;margin:0 auto;max-width:calc( var(--k-container-max-width) + calc(var(--k-container-padding) * 2) );padding:0 var(--k-container-padding);width:100%;}/*!sc*/
@media (min-width: 768px){.ivbozM{--k-container-padding:0px;}}/*!sc*/
data-styled.g71[id="Containerstyles-sc-11hjsrs-0"]{content:"dufmut,ivbozM,"}/*!sc*/
.jsGKVS{padding:0;color:var(--text-default);transition:color 350ms ease;}/*!sc*/
.jsGKVS:hover,.jsGKVS:focus{color:var(--text-primary);}/*!sc*/
data-styled.g97[id="SocialStyles__StyledSocial-sc-cc3469ac-0"]{content:"jsGKVS,"}/*!sc*/
.cHPtwG{transform-box:fill-box;transform-origin:0 0;transition:stroke-dashoffset 750ms cubic-bezier(0.68, -0.6, 0.32, 1.6),stroke-dasharray 750ms cubic-bezier(0.68, -0.6, 0.32, 1.6),transform 375ms cubic-bezier(0.68, -0.6, 0.32, 1.6);}/*!sc*/
data-styled.g98[id="DigitalOceanSmileyStyles__StyledCircle-sc-64ca7b97-0"]{content:"cHPtwG,"}/*!sc*/
.bgucfL{transform-box:fill-box;transform-origin:0 0;transition:transform 375ms cubic-bezier(0.68, -0.6, 0.32, 1.6) 375ms,opacity 187.5ms cubic-bezier(0.68, -0.6, 0.32, 1.6) 375ms;}/*!sc*/
data-styled.g99[id="DigitalOceanSmileyStyles__StyledPixelSm-sc-64ca7b97-1"]{content:"bgucfL,"}/*!sc*/
.fKJDss{transform-box:fill-box;transform-origin:0 100%;transition:transform 750ms cubic-bezier(0.68, -0.6, 0.32, 1.6);}/*!sc*/
data-styled.g100[id="DigitalOceanSmileyStyles__StyledPixelMd-sc-64ca7b97-2"]{content:"fKJDss,"}/*!sc*/
.gZIQKn{transform-box:fill-box;transform-origin:0 50%;transition:transform 750ms cubic-bezier(0.68, -0.6, 0.32, 1.6);}/*!sc*/
data-styled.g101[id="DigitalOceanSmileyStyles__StyledPixelLg-sc-64ca7b97-3"]{content:"gZIQKn,"}/*!sc*/
.bcPVou{cursor:pointer;overflow:visible;}/*!sc*/
.bcPVou:hover .DigitalOceanSmileyStyles__StyledCircle-sc-64ca7b97-0,.bcPVou:focus .DigitalOceanSmileyStyles__StyledCircle-sc-64ca7b97-0{stroke-dasharray:113.88273369263 113.88273369263;stroke-dashoffset:0;transform:translate(0,-13.75px);transition:stroke-dashoffset 750ms cubic-bezier(0.68, -0.6, 0.32, 1.6),stroke-dasharray 750ms cubic-bezier(0.68, -0.6, 0.32, 1.6),transform 375ms cubic-bezier(0.68, -0.6, 0.32, 1.6) 375ms;}/*!sc*/
.bcPVou:hover .DigitalOceanSmileyStyles__StyledPixelSm-sc-64ca7b97-1,.bcPVou:focus .DigitalOceanSmileyStyles__StyledPixelSm-sc-64ca7b97-1{opacity:0;transform:scale(0);transition:transform 375ms cubic-bezier(0.68, -0.6, 0.32, 1.6) 0ms,opacity 187.5ms cubic-bezier(0.68, -0.6, 0.32, 1.6) 562.5ms;}/*!sc*/
.bcPVou:hover .DigitalOceanSmileyStyles__StyledPixelMd-sc-64ca7b97-2,.bcPVou:focus .DigitalOceanSmileyStyles__StyledPixelMd-sc-64ca7b97-2{transform:translate(3.25px,-58.5px) translate(0,3.75px) scale(1.2777777777777777);}/*!sc*/
.bcPVou:hover .DigitalOceanSmileyStyles__StyledPixelLg-sc-64ca7b97-3,.bcPVou:focus .DigitalOceanSmileyStyles__StyledPixelLg-sc-64ca7b97-3{transform:translate(27.75px,-41.25px);}/*!sc*/
.bcPVou:focus{outline:none;}/*!sc*/
@media (hover:hover){.bcPVou:focus .DigitalOceanSmileyStyles__StyledPixelLg-sc-64ca7b97-3{animation:375ms cubic-bezier(0.68, -0.6, 0.32, 1.6) 0s 2 alternate lRCJp;}}/*!sc*/
data-styled.g102[id="DigitalOceanSmileyStyles__StyledSvg-sc-64ca7b97-4"]{content:"bcPVou,"}/*!sc*/
.FTZGU{align-items:center;display:flex;flex-direction:column;gap:32px;justify-content:space-between;margin:80px 0 0;}/*!sc*/
@media (min-width:768px){.FTZGU{flex-direction:row;}}/*!sc*/
data-styled.g103[id="CompanyDetailsStyles__StyledCompanyDetails-sc-6238711b-0"]{content:"FTZGU,"}/*!sc*/
.cPMjKd{align-items:center;display:flex;flex-wrap:wrap;gap:16px;justify-content:center;text-align:center;}/*!sc*/
@media (min-width:768px){.cPMjKd{flex-wrap:nowrap;}}/*!sc*/
.cPMjKd svg{color:var(--logo-do-blue);}/*!sc*/
.cPMjKd a{color:var(--text-default);}/*!sc*/
.cPMjKd a:hover{color:var(--text-primary);}/*!sc*/
data-styled.g104[id="CompanyDetailsStyles__StyledCompanyLogo-sc-6238711b-1"]{content:"cPMjKd,"}/*!sc*/
.fCORkn{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;list-style:none;margin:0;max-width:12rem;padding:0;}/*!sc*/
@media (min-width:768px){.fCORkn{max-width:none;}}/*!sc*/
data-styled.g105[id="CompanyDetailsStyles__StyledCompanySocials-sc-6238711b-2"]{content:"fCORkn,"}/*!sc*/
.biKpFd{display:none;gap:32px;grid-template-columns:repeat(auto-fill,minmax(192px,1fr));width:100%;}/*!sc*/
@media (min-width:768px){.biKpFd{display:grid;}}/*!sc*/
data-styled.g106[id="LinksStyles__StyledFooterDesktop-sc-ba6fe185-0"]{content:"biKpFd,"}/*!sc*/
.kPlCIK{display:flex;flex-direction:column;gap:8px;list-style:none;margin:16px 0 0;padding:0;}/*!sc*/
data-styled.g107[id="LinksStyles__StyledList-sc-ba6fe185-1"]{content:"kPlCIK,"}/*!sc*/
.joqZnf:hover,.joqZnf:focus{color:var(--text-primary);}/*!sc*/
data-styled.g108[id="LinksStyles__StyledLink-sc-ba6fe185-2"]{content:"joqZnf,"}/*!sc*/
.NApBt{display:flex;flex-direction:column;width:100%;}/*!sc*/
@media (min-width:768px){.NApBt{display:none;}}/*!sc*/
.NApBt details:not(:last-child){border-bottom:1px solid;}/*!sc*/
.NApBt .LinksStyles__StyledList-sc-ba6fe185-1{margin:0 0 16px;}/*!sc*/
data-styled.g109[id="LinksStyles__StyledFooterMobile-sc-ba6fe185-3"]{content:"NApBt,"}/*!sc*/
.kqYPUz{cursor:pointer;}/*!sc*/
.kqYPUz summary{align-items:center;display:flex;justify-content:space-between;list-style:none;padding:16px 0;}/*!sc*/
.kqYPUz summary::-webkit-details-marker{display:none;}/*!sc*/
.kqYPUz summary .up,.kqYPUz summary .down{color:var(--text-primary);flex:0 0 auto;}/*!sc*/
.kqYPUz[open] summary .down{display:none;}/*!sc*/
.kqYPUz:not([open]) summary .up{display:none;}/*!sc*/
data-styled.g110[id="LinksStyles__StyledDetails-sc-ba6fe185-4"]{content:"kqYPUz,"}/*!sc*/
.kVyktB{display:none;}/*!sc*/
@media (min-width:768px){.kVyktB{display:inline-flex;}}/*!sc*/
data-styled.g111[id="DigitalOceanStyles__StyledText-sc-5322d8c4-0"]{content:"kVyktB,"}/*!sc*/
.gNLfcd{color:var(--logo-do-blue);display:inline-flex;}/*!sc*/
data-styled.g112[id="DigitalOceanStyles__StyledLogo-sc-5322d8c4-1"]{content:"gNLfcd,"}/*!sc*/
.jkqhgD{isolation:isolate;position:sticky;top:0;z-index:1000;}/*!sc*/
.jkqhgD header{z-index:1000;}/*!sc*/
data-styled.g113[id="HeaderStyles__StyledHeader-sc-c7d2c41b-0"]{content:"jkqhgD,"}/*!sc*/
.bRnkwC{display:flex;flex-direction:column;gap:8px;list-style-type:none;padding:0;white-space:nowrap;}/*!sc*/
@media (min-width:calc(768px)){.bRnkwC{flex-direction:row;}}/*!sc*/
@media (max-width:calc(768px - 1px)){.bRnkwC{gap:16px;}}/*!sc*/
@media (max-width:calc(768px - 1px)){.bRnkwC >li:first-child>a,.bRnkwC >li:first-child>button{box-shadow:0 0 0 1px var(--text-default);color:var(--text-default);}.bRnkwC >li:first-child>a:hover,.bRnkwC >li:first-child>button:hover{background-color:transparent;}}/*!sc*/
@media (max-width:calc(1024px - 1px)){.bRnkwC >li{flex-basis:0;flex-grow:1;}.bRnkwC >li >a,.bRnkwC >li >button{text-align:center;width:100%;}}/*!sc*/
.bRnkwC button{align-items:center;display:flex;gap:2px;}/*!sc*/
.bRnkwC button svg{flex-shrink:0;}/*!sc*/
data-styled.g114[id="HeaderStyles__StyledCTALinks-sc-c7d2c41b-1"]{content:"bRnkwC,"}/*!sc*/
.eFxNdr{background:linear-gradient(90deg,
#FFC001 0%,
#D4DF00 16.15%,
#80D34A 33.85%,
#00C483 50.52%,
#0BE1FF 66.15%,
#4ABEFF 82.52%,
#0069FF 100%
);clip-path:polygon(0% 0%,var(--progress-width,0) 0%,var(--progress-width,0) 100%,0% 100%);height:8px;left:0;position:absolute;top:100%;width:100%;will-change:clip-path;z-index:1;}/*!sc*/
data-styled.g117[id="HeaderStyles__StyledProgressBar-sc-c7d2c41b-4"]{content:"eFxNdr,"}/*!sc*/
.rcxBJ{background-color:var(--navigation-tophat-background);display:none;padding:8px 0;visibility:hidden;}/*!sc*/
@media (min-width: 768px){.rcxBJ{display:block;visibility:visible;}}/*!sc*/
data-styled.g147[id="TopBarstyles__StyledTopBar-sc-17n1n7p-0"]{content:"rcxBJ,"}/*!sc*/
.grsQFs{align-items:center;display:flex;gap:0 16px;line-height:0;margin:0 auto;max-width:1360px;padding:0 24px;}/*!sc*/
@media (min-width: 768px){.grsQFs{justify-content:center;}}/*!sc*/
data-styled.g148[id="TopBarstyles__StyledTopBarContainer-sc-17n1n7p-1"]{content:"grsQFs,"}/*!sc*/
.lwFrb{display:flex;flex:1 1 auto;flex-direction:column;min-height:1.375em;overflow:hidden;position:relative;}/*!sc*/
data-styled.g149[id="TopBarstyles__StyledTopBarCTAs-sc-17n1n7p-2"]{content:"lwFrb,"}/*!sc*/
.dFthev{display:none;list-style-type:none;margin:0;padding:0;}/*!sc*/
@media (min-width: 1024px){.dFthev{align-items:center;display:flex;flex:0 0 auto;gap:0 16px;}}/*!sc*/
.dFthev a{color:var(--text-on-color);display:block;text-align:center;transition:color 300ms ease-in-out;}/*!sc*/
.dFthev a:hover{text-decoration:underline;text-underline-offset:2px;}/*!sc*/
data-styled.g150[id="TopBarstyles__StyledTopBarLinks-sc-17n1n7p-3"]{content:"dFthev,"}/*!sc*/
.iffdiX{background-color:var(--background-default);overflow-x:clip;position:relative;z-index:100;}/*!sc*/
.iffdiX::after{background-color:var(--border-transparent);bottom:0;content:'';height:1px;left:0;pointer-events:none;position:absolute;width:100%;}/*!sc*/
data-styled.g152[id="Headerstyles__StyledHeader-sc-9ucsot-0"]{content:"iffdiX,"}/*!sc*/
.gXTzhN{align-items:center;display:flex;gap:16px;margin:0 auto;max-width:1440px;padding:16px 24px;}/*!sc*/
@media (min-width: 768px){.gXTzhN{gap:24px;padding:16px 64px;}}/*!sc*/
data-styled.g153[id="Headerstyles__StyledHeaderContainer-sc-9ucsot-1"]{content:"gXTzhN,"}/*!sc*/
.dMqhZP{line-height:0;margin-right:auto;}/*!sc*/
data-styled.g154[id="Headerstyles__StyledHeaderLogo-sc-9ucsot-2"]{content:"dMqhZP,"}/*!sc*/
.ewqLjr{color:var(--text-default);height:32px;padding:0;width:32px;}/*!sc*/
@media (min-width: 1024px){.ewqLjr{display:none;}}/*!sc*/
data-styled.g155[id="Headerstyles__StyledHeaderToggle-sc-9ucsot-3"]{content:"ewqLjr,"}/*!sc*/
.hPzTGD{display:none;}/*!sc*/
@media (min-width: 768px){.hPzTGD{display:block;margin-left:auto;}}/*!sc*/
data-styled.g156[id="Headerstyles__StyledHeaderContent-sc-9ucsot-4"]{content:"hPzTGD,"}/*!sc*/
.lXEKW{background-color:var(--border-subtle);border-radius:999px;display:none;height:24px;width:1.5px;}/*!sc*/
.Headerstyles__StyledHeaderUtilities-sc-9ucsot-5~.lXEKW{display:block;}/*!sc*/
@media (min-width: 1024px){.Headerstyles__StyledHeaderUtilities-sc-9ucsot-5~.lXEKW{display:none;}}/*!sc*/
@media (min-width: 768px){.lXEKW{display:block;}}/*!sc*/
@media (min-width: 1024px){.lXEKW{display:none;}}/*!sc*/
data-styled.g158[id="Headerstyles__StyledDivider-sc-9ucsot-6"]{content:"lXEKW,"}/*!sc*/
.dtnGwk{-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);background-color:rgba(255,255,255,0.1);height:calc(100% - 40px);left:0;opacity:0;pointer-events:none;position:fixed;top:40px;transition:opacity 300ms ease-in-out;width:100%;z-index:-1;}/*!sc*/
data-styled.g159[id="Headerstyles__StyledBackdrop-sc-9ucsot-7"]{content:"dtnGwk,"}/*!sc*/
.QRNWP{flex-shrink:0;opacity:1;z-index:3;}/*!sc*/
.QRNWP svg{height:20px;width:20px;}/*!sc*/
@media (min-width: 1024px){.QRNWP{opacity:0;transform:translateX(-8px);transition:transform 300ms ease-in-out,opacity 300ms ease-in-out;will-change:transform,opacity;}}/*!sc*/
data-styled.g161[id="Cardstyles__StyledChevron-sc-ngsvtw-0"]{content:"QRNWP,"}/*!sc*/
.ieFyWy{align-items:center;border-radius:8px;display:flex;flex-shrink:0;gap:12px;justify-content:space-between;overflow:hidden;padding:12px 8px;position:relative;transition:background-color 300ms ease-in-out;}/*!sc*/
.ieFyWy:hover{background-color:var(--navigation-www-nav-card-hover);cursor:pointer;}/*!sc*/
@media (hover:hover) and (pointer:fine){.ieFyWy:hover .Cardstyles__StyledChevron-sc-ngsvtw-0{opacity:1;transform:translateX(0);}}/*!sc*/
data-styled.g162[id="Cardstyles__StyledCard-sc-ngsvtw-1"]{content:"ieFyWy,"}/*!sc*/
.klxEek{display:flex;flex-direction:column;position:relative;z-index:2;}/*!sc*/
data-styled.g163[id="Cardstyles__StyledCardContentContainer-sc-ngsvtw-2"]{content:"klxEek,"}/*!sc*/
.ilYFpC{align-items:center;display:flex;gap:8px;}/*!sc*/
.ilYFpC svg{color:var(--icon-brand);flex-shrink:0;height:auto;width:32px;}/*!sc*/
data-styled.g164[id="Cardstyles__StyledCardHeading-sc-ngsvtw-3"]{content:"ilYFpC,"}/*!sc*/
.bbcngE{display:flex;flex-direction:column;gap:8px;}/*!sc*/
@media (min-width: 1024px){.bbcngE{display:none;}}/*!sc*/
data-styled.g165[id="Cardstyles__StyledCardContent-sc-ngsvtw-4"]{content:"bbcngE,"}/*!sc*/
.jfWvYI{display:flex;flex-direction:column;height:100%;margin:0 auto;max-width:1440px;width:100%;}/*!sc*/
@media (min-width: 1024px){.jfWvYI{flex-direction:row;gap:24px;height:620px;padding:24px 40px;}}/*!sc*/
@media (min-width: 1280px){.jfWvYI{height:486px;padding:32px 48px;}}/*!sc*/
@media (min-width: 1440px){.jfWvYI{height:464px;}}/*!sc*/
data-styled.g167[id="Dropdownstyles__StyledDropdownContainer-sc-16wobc6-0"]{content:"jfWvYI,"}/*!sc*/
.hwyAqH{background-color:var(--background-default);display:none;height:calc(100dvh - 64px);left:0;line-height:1;overflow:hidden;position:absolute;top:0;width:100%;z-index:100;}/*!sc*/
@media (min-width: 768px){.hwyAqH{background-color:var(--background-default);border-radius:0 0 24px 24px;box-shadow:8px 8px 12px 0 light-dark(rgba(0, 12, 42, 0.1), rgba(247, 248, 251, 0.1));height:auto;}}/*!sc*/
@media (min-width: 1024px){.hwyAqH{display:block;height:0;opacity:0;top:100%;transition:opacity 300ms ease-in-out 300ms;}}/*!sc*/
data-styled.g168[id="Dropdownstyles__StyledDropdown-sc-16wobc6-1"]{content:"hwyAqH,"}/*!sc*/
.lmXcfw{display:none;}/*!sc*/
@media (min-width: 1024px){.lmXcfw{display:flex;flex-direction:column;gap:4px;padding:16px 8px 0;}}/*!sc*/
data-styled.g171[id="Dropdownstyles__StyledDropdownHeadingContainer-sc-16wobc6-4"]{content:"lmXcfw,"}/*!sc*/
.fVUyrn{height:100%;overflow:auto;transform:translateX(0);transition:transform 300ms ease-in-out;}/*!sc*/
@media (min-width: 768px){.fVUyrn{height:auto;}}/*!sc*/
@media (min-width: 1024px){.fVUyrn{background-color:var(--background-card);border:1px solid var(--border-transparent);border-radius:16px;height:100%;max-height:100%;max-width:320px;padding:16px;transform:translateX(0);width:100%;}}/*!sc*/
data-styled.g173[id="Dropdownstyles__StyledFeature-sc-16wobc6-6"]{content:"fVUyrn,"}/*!sc*/
.bzgLAA{display:flex;flex-direction:column;flex-shrink:0;gap:16px;height:100%;max-height:100%;overflow-y:auto;padding:0 2px 24px 24px;scrollbar-gutter:stable;}/*!sc*/
.bzgLAA::-webkit-scrollbar{appearance:none;}/*!sc*/
.bzgLAA::-webkit-scrollbar:vertical{width:8px;}/*!sc*/
.bzgLAA::-webkit-scrollbar-track{background:transparent;border:none;box-shadow:none;}/*!sc*/
.bzgLAA::-webkit-scrollbar-thumb{background-color:var(--border-subtle);border:2px solid var(--border-subtle);border-radius:999px;}/*!sc*/
.bzgLAA .Cardstyles__StyledCard-sc-ngsvtw-1{padding:12px;}/*!sc*/
@media (min-width: 1024px){.bzgLAA{padding:0 16px 0 0;}.bzgLAA .Cardstyles__StyledCard-sc-ngsvtw-1{padding:8px 12px;}}/*!sc*/
data-styled.g174[id="Dropdownstyles__StyledFeatureInner-sc-16wobc6-7"]{content:"bzgLAA,"}/*!sc*/
.kLnAor{display:none;flex-direction:column;gap:24px;height:0;max-height:calc(100% - 64px);overflow:auto;padding:0;transform:translateX(100%);transition:transform 300ms ease-in-out;}/*!sc*/
@media (min-width: 768px){.kLnAor{height:0;}}/*!sc*/
@media (min-width: 1024px){.kLnAor{max-height:none;padding:0;transform:translateX(0);}}/*!sc*/
data-styled.g175[id="Dropdownstyles__StyledDropdownContent-sc-16wobc6-8"]{content:"kLnAor,"}/*!sc*/
.ZXGbs{margin-top:auto;}/*!sc*/
@media (min-width: 768px){.ZXGbs{flex:1;margin-top:0;}}/*!sc*/
.ZXGbs a{align-items:center;display:flex;gap:8px;justify-content:center;width:100%;}/*!sc*/
.ZXGbs a svg{width:16px;}/*!sc*/
data-styled.g177[id="Dropdownstyles__StyledButton-sc-16wobc6-10"]{content:"ZXGbs,"}/*!sc*/
.eGyFzQ{padding:24px 24px 0 24px;}/*!sc*/
@media (min-width: 1024px){.eGyFzQ{display:none;}}/*!sc*/
.eGyFzQ svg:last-of-type{flex-shrink:0;}/*!sc*/
data-styled.g179[id="Dropdownstyles__StyledBreadcrumbContainer-sc-16wobc6-12"]{content:"eGyFzQ,"}/*!sc*/
.fkPxaf{flex-grow:1;z-index:100;}/*!sc*/
@media screen and (max-width:calc(604px - 1px)){.fkPxaf{height:calc(100vh - 64px);}}/*!sc*/
@media screen and (max-width:calc(1024px - 1px)){.fkPxaf{background-color:var(--background-default);border-radius:0 0 24px 24px;box-shadow:8px 8px 12px 0 light-dark(rgba(0, 12, 42, 0.1), rgba(247, 248, 251, 0.1));left:0;padding:24px;position:absolute;top:100%;transform:translateX(100%);transition:transform 300ms ease-in-out;width:100%;}.fkPxaf body{overflow-x:hidden;}}/*!sc*/
data-styled.g180[id="Navigationstyles__StyledNavigation-sc-16d688r-0"]{content:"fkPxaf,"}/*!sc*/
.eXFlDd{display:flex;flex-direction:column;gap:40px;height:100%;justify-content:space-between;}/*!sc*/
@media (min-width: 1024px){.eXFlDd{align-items:center;flex-direction:row;gap:0;}}/*!sc*/
data-styled.g181[id="Navigationstyles__StyledNavigationContainer-sc-16d688r-1"]{content:"eXFlDd,"}/*!sc*/
.ekrhbo{display:flex;flex-direction:column;gap:16px;list-style-type:none;margin:0;padding:0;}/*!sc*/
@media (min-width: 1024px){.ekrhbo{align-items:center;flex-direction:row;flex-grow:1;gap:0;}}/*!sc*/
data-styled.g182[id="Navigationstyles__StyledNavigationList-sc-16d688r-2"]{content:"ekrhbo,"}/*!sc*/
@media (min-width: 1024px){.jtJtVa{border-bottom:0;}.jtJtVa >a,.jtJtVa >button{transition:background-color 300ms ease-in-out,color 300ms ease-in-out;}.jtJtVa svg{flex-shrink:0;}@media (scripting:none){.jtJtVa .Dropdownstyles__StyledDropdown-sc-16wobc6-1{background-color:var(--background-default);}.jtJtVa:hover .Dropdownstyles__StyledDropdown-sc-16wobc6-1,.jtJtVa:focus-within .Dropdownstyles__StyledDropdown-sc-16wobc6-1{clip-path:polygon(0 0,100% 0,100% 100%,0 100%);opacity:1;}.jtJtVa:hover >a,.jtJtVa:focus-within >a,.jtJtVa:hover >button,.jtJtVa:focus-within >button{background-color:var(--navigation-www-nav-card-hover);color:var(--text-primary);}.jtJtVa:hover >a svg,.jtJtVa:focus-within >a svg,.jtJtVa:hover >button svg,.jtJtVa:focus-within >button svg{transform:rotate(180deg);}}}/*!sc*/
@media (min-width: 1024px){.jtJtVa:first-child{margin-left:auto;}}/*!sc*/
@media (min-width: 1024px){.jtJtVa:last-child{margin-right:auto;}}/*!sc*/
.jtJtVa >a,.jtJtVa >button{align-items:center;border-radius:999px;color:var(--text-primary);display:flex;gap:2px;justify-content:space-between;padding:12px;position:relative;width:100%;}/*!sc*/
@media (min-width: 1024px){.jtJtVa >a,.jtJtVa >button{color:var(--text-default);justify-content:flex-start;padding:8px 16px;width:auto;}}/*!sc*/
.jtJtVa >a::before,.jtJtVa >button::before{content:'';height:calc(100% + 16px);left:0;position:absolute;top:0;width:100%;}/*!sc*/
.jtJtVa >a svg,.jtJtVa >button svg{transform:rotate(-90deg);transition:transform 300ms ease-in-out;}/*!sc*/
@media (min-width: 1024px){.jtJtVa >a svg,.jtJtVa >button svg{transform:rotate(0);}}/*!sc*/
@media (min-width: 1024px){.eqPzQX{border-bottom:0;}.eqPzQX >a,.eqPzQX >button{transition:background-color 300ms ease-in-out,color 300ms ease-in-out;}.eqPzQX svg{flex-shrink:0;}.eqPzQX::after{opacity:1;}.eqPzQX:hover >a,.eqPzQX:focus-within >a,.eqPzQX:hover >button,.eqPzQX:focus-within >button{background-color:var(--navigation-www-nav-card-hover);color:var(--text-primary);}.eqPzQX:hover >a svg,.eqPzQX:focus-within >a svg,.eqPzQX:hover >button svg,.eqPzQX:focus-within >button svg{transform:rotate(180deg);}@media (scripting:none){.eqPzQX .Dropdownstyles__StyledDropdown-sc-16wobc6-1{background-color:var(--background-default);}.eqPzQX:hover .Dropdownstyles__StyledDropdown-sc-16wobc6-1,.eqPzQX:focus-within .Dropdownstyles__StyledDropdown-sc-16wobc6-1{clip-path:polygon(0 0,100% 0,100% 100%,0 100%);opacity:1;}.eqPzQX:hover >a,.eqPzQX:focus-within >a,.eqPzQX:hover >button,.eqPzQX:focus-within >button{background-color:var(--navigation-www-nav-card-hover);color:var(--text-primary);}.eqPzQX:hover >a svg,.eqPzQX:focus-within >a svg,.eqPzQX:hover >button svg,.eqPzQX:focus-within >button svg{transform:rotate(180deg);}}}/*!sc*/
@media (min-width: 1024px){.eqPzQX:first-child{margin-left:auto;}}/*!sc*/
@media (min-width: 1024px){.eqPzQX:last-child{margin-right:auto;}}/*!sc*/
.eqPzQX >a,.eqPzQX >button{align-items:center;border-radius:999px;color:var(--text-primary);display:flex;gap:2px;justify-content:space-between;padding:12px;position:relative;width:100%;}/*!sc*/
@media (min-width: 1024px){.eqPzQX >a,.eqPzQX >button{color:var(--text-default);justify-content:flex-start;padding:8px 16px;width:auto;}}/*!sc*/
.eqPzQX >a::before,.eqPzQX >button::before{content:'';height:calc(100% + 16px);left:0;position:absolute;top:0;width:100%;}/*!sc*/
.eqPzQX >a svg,.eqPzQX >button svg{transform:rotate(-90deg);transition:transform 300ms ease-in-out;}/*!sc*/
@media (min-width: 1024px){.eqPzQX >a svg,.eqPzQX >button svg{transform:rotate(0);}}/*!sc*/
data-styled.g183[id="Navigationstyles__StyledNavigationItem-sc-16d688r-3"]{content:"jtJtVa,eqPzQX,"}/*!sc*/
@media (min-width: 768px){.bhcsEb{display:none;}}/*!sc*/
data-styled.g184[id="Navigationstyles__StyledNavigationContent-sc-16d688r-4"]{content:"bhcsEb,"}/*!sc*/
.eDFQJ{display:none;}/*!sc*/
@media (min-width: 1024px){.eDFQJ{background-color:var(--background-default);display:block;height:0;left:0;position:absolute;top:100%;transition:height 300ms ease-in-out;width:100%;}@media (prefers-reduced-motion){.eDFQJ{transition:none;}}}/*!sc*/
data-styled.g185[id="Navigationstyles__StyledNavigationBackground-sc-16d688r-5"]{content:"eDFQJ,"}/*!sc*/
:root{color-scheme:light;}/*!sc*/
html{--top-hat-height:calc(0 * 1px);--primary-nav-height:73px;--sub-nav-height:calc(0 * 1px);--content-spacing:64px;--scroll-padding-top:calc( var(--top-hat-height) + var(--primary-nav-height) + var(--sub-nav-height) + var(--content-spacing) );scroll-behavior:smooth;scroll-padding-top:var(--scroll-padding-top);}/*!sc*/
body{background-color:var(--background-default);line-height:1.4;text-rendering:optimizeLegibility;}/*!sc*/
ol,ul{list-style:none;margin:0;padding:0;}/*!sc*/
table{border-collapse:collapse;}/*!sc*/
h1,h2,h3,h4,h5{font-family:'Plus Jakarta Sans',sans-serif;}/*!sc*/
.truste_box_overlay{left:200vw;position:fixed;}/*!sc*/
.truste_overlay{display:none;}/*!sc*/
.truste_box_overlay.slide-up{animation:ckkqjM 1s forwards;left:0;max-height:calc(100% - 40px);overflow:auto;}/*!sc*/
.truste_overlay.fade-in{animation:kVaHQg 1s forwards;display:block;}/*!sc*/
#truste-consent-track{left:200vw;}/*!sc*/
#truste-consent-track.slide-up{animation:ckkqjM 1s forwards;}/*!sc*/
data-styled.g188[id="sc-global-dKQesU1"]{content:"sc-global-dKQesU1,"}/*!sc*/
:root{--algae-100:#E1E6C2;--algae-200:#C3CE85;--algae-300:#A6B559;--algae-400:#94A54B;--algae-50:#F2F4E6;--algae-500:#879B42;--algae-600:#6C7E35;--algae-700:#525F28;--algae-800:#38401B;--algae-900:#1D210E;--category-bitter-lemon-100:#D4DF00;--category-bitter-lemon-200:#F3FF0B;--category-bitter-lemon-300:#FBFFB5;--category-bitter-lemon-400:#FEFFF4;--category-guppie-green-100:#0BFF8A;--category-guppie-green-200:#75FFBD;--category-guppie-green-300:#B5FFDB;--category-guppie-green-400:#F4FFFA;--category-guppie-green-92:#0AEA7E;--category-jordy-blue-100:#8AABFF;--category-jordy-blue-200:#CAD9FF;--category-jordy-blue-300:#DFE8FF;--category-jordy-blue-400:#F4F7FF;--category-jordy-blue-92:#7F9DEA;--category-kiwi-100:#80D34A;--category-kiwi-200:#B1E490;--category-kiwi-300:#D5F0C3;--category-kiwi-400:#F9FDF6;--category-kiwi-92:#76C244;--category-lake-100:#4ABEFF;--category-lake-200:#9FDDFF;--category-lake-300:#CAECFF;--category-lake-400:#F4FBFF;--category-lake-92:#44AFEA;--category-lavender-100:#E88AFF;--category-lavender-200:#F0B5FF;--category-lavender-300:#F9DFFF;--category-lavender-400:#FDF4FF;--category-lavender-92:#D57FEB;--category-lilac-100:#BBA7F7;--category-lilac-200:#D9CEFB;--category-lilac-300:#E8E2FC;--category-lilac-400:#F7F5FE;--category-lilac-92:#AC9AE3;--category-metallic-yellow-100:#FFC90B;--category-metallic-yellow-200:#FFE175;--category-metallic-yellow-300:#FFEFB5;--category-metallic-yellow-400:#FFFDF4;--category-metallic-yellow-92:#EAB90A;--category-mustard-100:#FFE50B;--category-mustard-200:#FFF075;--category-mustard-300:#FFF7B5;--category-mustard-400:#FFFEF4;--category-pink-elephant-100:#FF9FEA;--category-pink-elephant-200:#FFB5EF;--category-pink-elephant-300:#FFCAF3;--category-pink-elephant-400:#FFF4FD;--category-pink-elephant-92:#EA92D7;--category-sea-sky-100:#00F4C8;--category-sea-sky-200:#75FFE6;--category-sea-sky-300:#B5FFF1;--category-sea-sky-400:#F4FFFD;--category-sea-sky-92:#00E0B8;--category-spray-tan-100:#FFA14A;--category-spray-tan-200:#FFB775;--category-spray-tan-300:#FFD8B5;--category-spray-tan-400:#FFF9F4;--category-spray-tan-92:#EA9444;--category-tulip-100:#FF928A;--category-tulip-200:#FFBAB5;--category-tulip-300:#FFE1DF;--category-tulip-400:#FFF5F4;--category-vivid-sky-100:#0BE1FF;--category-vivid-sky-200:#75EEFF;--category-vivid-sky-300:#B5F6FF;--category-vivid-sky-400:#F4FEFF;--category-vivid-sky-92:#0ACFEA;--cerulean-100:#C6DDF8;--cerulean-200:#8DBAF1;--cerulean-300:#5198FB;--cerulean-400:#2E85E0;--cerulean-50:#E8F1FC;--cerulean-500:#1E7ADB;--cerulean-600:#1862B0;--cerulean-700:#124984;--cerulean-800:#0C3158;--cerulean-900:#06182C;--color-primary-gray-1:#000C2A;--color-primary-gray-6:#A9B3CA;--coral-100:#ECC9C0;--coral-200:#D8907E;--coral-300:#BE6450;--coral-400:#B2543E;--coral-50:#F8EBE7;--coral-500:#A54A34;--coral-600:#843A29;--coral-700:#632C1F;--coral-800:#421D14;--coral-900:#210F0A;--deep-00:#000A0A;--deep-100:#000F0F;--deep-1000:#F4F5F5;--deep-200:#081F1E;--deep-300:#13302E;--deep-400:#1F403E;--deep-50:#000000;--deep-500:#325553;--deep-600:#4D716E;--deep-700:#6F908C;--deep-800:#9DB5B2;--deep-900:#C9D6D4;--deep-950:#E5ECEB;--deep-deep-1000-10:rgba(244, 245, 245, 0.1);--deep-deep-1000-20:rgba(244, 245, 245, 0.2);--deep-deep-50-80:rgba(0, 0, 0, 0.8);--expanded-dragonfruit-100:#B458FC;--expanded-green-apple-100:#00D688;--expanded-green-apple-92:#00C57D;--expanded-honeydew-100:#FFC001;--expanded-lime-100:#80D34A;--expanded-orange-100:#FF720E;--expanded-pear-100:#D7E200;--expanded-raspberry-100:#FF4C6C;--foam-100:#C9EEF2;--foam-200:#6FE0ED;--foam-300:#30CBD9;--foam-400:#1AAFBF;--foam-50:#ECF9FB;--foam-500:#237F8C;--foam-600:#196571;--foam-700:#104B55;--foam-800:#08333A;--foam-900:#041A1F;--kelp-100:#C8DECB;--kelp-200:#8FBC95;--kelp-300:#5A9C63;--kelp-400:#428A4C;--kelp-50:#E9F2EA;--kelp-500:#397A41;--kelp-600:#2E6234;--kelp-700:#224A27;--kelp-800:#17321B;--kelp-900:#0B190D;--primary-black:#000000;--primary-blue-100:#1433D6;--primary-blue-200:#0069FF;--primary-blue-250:#0092FF;--primary-blue-300:#C6E3FF;--primary-blue-50:#000C79;--primary-cyan:#45CAC1;--primary-fuchsia-100:#8917A6;--primary-fuchsia-200:#CA64DD;--primary-fuchsia-300:#EB
