import mediafire_dl

urls = '''
https://www.mediafire.com/file/tbsjink7k3sxziv/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_20210815a.part1.rar/file	https://www.mediafire.com/file/l57ooctcaegqhdw/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_20210815a.part2.rar/file	https://www.mediafire.com/file/xgrn52svti8g6ek/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_20210815a.part3.rar/file
https://www.mediafire.com/file/7nmyn0tkqy3t3gu/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Backout_Queen_Misa.part1.rar/file	https://www.mediafire.com/file/hkdix54ij0iuzrf/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Backout_Queen_Misa.part2.rar/file	https://www.mediafire.com/file/ueiliyuiwffbpo6/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Backout_Queen_Misa.part3.rar/file
https://www.mediafire.com/file/i5h4xn4buaix4nj/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Maid_Mansion_N%25C2%25BA2.part1.rar/file	https://www.mediafire.com/file/i7417hkcvy2tpjo/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Maid_Mansion_N%25C2%25BA2.part2.rar/file	https://www.mediafire.com/file/s1pl9gc3mdf0ak9/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Maid_Mansion_N%25C2%25BA2.part3.rar/file
https://www.mediafire.com/file/2tp5nvwv2e5bswy/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Loose_and_Tight_Violet.part1.rar/file	https://www.mediafire.com/file/0v3i1g6319ruc12/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Loose_and_Tight_Violet.part2.rar/file	https://www.mediafire.com/file/i9yue18p8n7nnqf/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Loose_and_Tight_Violet.part3.rar/file
https://www.mediafire.com/file/uvgma9w44a41rkz/DJAWA_Photo_-_Aram_%2528%25EC%2595%2584%25EB%259E%258C%2529_-_Creamy_Alice.part1.rar/file	https://www.mediafire.com/file/y5piu2m549qnxwz/DJAWA_Photo_-_Aram_%2528%25EC%2595%2584%25EB%259E%258C%2529_-_Creamy_Alice.part2.rar/file	
https://www.mediafire.com/file/bhuq1jnzsa6q7os/DAA20220223.part1.rar/file	https://www.mediafire.com/file/w2b3duwgzsiyu0d/DAA20220223.part2.rar/file	
https://www.mediafire.com/file/fdn3hvteu1sscue/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210716a.part1.rar/file	https://www.mediafire.com/file/veueegat30iy14i/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210716a.part2.rar/file	
https://www.mediafire.com/file/xljmrfgjb1thdyj/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_iila_illa.part1.rar/file	https://www.mediafire.com/file/p39wuynprxagbwz/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_iila_illa.part2.rar/file	
https://www.mediafire.com/file/q9s0jtcrmv63nh1/DJAWA_Photo_-_HaNari_%2528%25ED%2595%2598%25EB%2582%2598%25EB%25A6%25AC%2529_-_Loose_and_Tight_Cool_Mint.part1.rar/file	https://www.mediafire.com/file/o5z66xcdf8t3ncz/DJAWA_Photo_-_HaNari_%2528%25ED%2595%2598%25EB%2582%2598%25EB%25A6%25AC%2529_-_Loose_and_Tight_Cool_Mint.part2.rar/file	
https://www.mediafire.com/file/c7p7s1czwrw749v/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_The_cat_I_picked_up_turned_into_a_girl.part1.rar/file	https://www.mediafire.com/file/nl2mp3ex6y4gc2x/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_The_cat_I_picked_up_turned_into_a_girl.part2.rar/file	
https://www.mediafire.com/file/2izwslldmqzhmme/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Rudy_The_Wolf_of_Midnight.part1.rar/file	https://www.mediafire.com/file/n8483540rp4ilks/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Rudy_The_Wolf_of_Midnight.part2.rar/file	
https://www.mediafire.com/file/bzmkl5myjufrwtf/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Combat_Maid_Mansion.part1.rar/file	https://www.mediafire.com/file/hronygbmrl09hxz/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Combat_Maid_Mansion.part2.rar/file	
https://www.mediafire.com/file/a44w0il51vty767/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Football_Star.part1.rar/file	https://www.mediafire.com/file/gc01wftwzlr3rqc/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Football_Star.part2.rar/file	
https://www.mediafire.com/file/pk8y9krasg6lsd4/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Christmas_Special_2021.part1.rar/file	https://www.mediafire.com/file/dhf1kimbbwy3u95/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Christmas_Special_2021.part2.rar/file	
https://www.mediafire.com/file/3didv787kvbl3oq/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Moral_Guardian_of_School.part1.rar/file	https://www.mediafire.com/file/c3fve6ijf7u2pb6/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Moral_Guardian_of_School.part2.rar/file	
https://www.mediafire.com/file/u24v7nrptsi2wmr/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Refreshing_Summer.part1.rar/file	https://www.mediafire.com/file/9uy9c3ja293guwc/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Refreshing_Summer.part2.rar/file	
https://www.mediafire.com/file/2tt0nss5b0mckz0/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Loose_and_Tight_Pink.part1.rar/file	https://www.mediafire.com/file/4wfgkkmw6zp4ef7/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Loose_and_Tight_Pink.part2.rar/file	
https://www.mediafire.com/file/nx49zvpc4w9uqfy/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Succubus_2B.part1.rar/file	https://www.mediafire.com/file/4lye0g83bgp4c49/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Succubus_2B.part2.rar/file	
https://www.mediafire.com/file/1pcki01qy0b8ej0/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_St._Esther.part1.rar/file	https://www.mediafire.com/file/33z1yufuqejx8y2/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_St._Esther.part2.rar/file	
https://www.mediafire.com/file/q9rnfrotj92xkej/DJAWA_Photo_-_Aram_%2528%25EC%2595%2584%25EB%259E%258C%2529_20210829a.rar/file		
https://www.mediafire.com/file/6dt25dhoi11ytrn/DJAWA_Photo_-_Aram_%2528%25EC%2595%2584%25EB%259E%258C%2529_-_Queen_of_Thorns.rar/file		
https://www.mediafire.com/file/h7gcvfp362zk9ar/DJAWA_Photo_-_Aram_%2528%25EC%2595%2584%25EB%259E%258C%2529_-_%25E2%2580%259CHot_Pink_Jersey%2521%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/68scktnijj27gue/DJAWA_Photo_-_Aram_%2528%25EC%2595%2584%25EB%259E%258C%2529_20210821a.rar/file		
https://www.mediafire.com/file/9obhdupopj2gb7t/DJAWA_Photo_-_Aya.rar/file		
https://www.mediafire.com/file/78vlmrrguiulsqq/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_%2526_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_-_Maid_Mansion_W.rar/file		
https://www.mediafire.com/file/u5czo9kz4xs6yz3/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210721a.rar/file		
https://www.mediafire.com/file/n3lqhjbwmpqhugg/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Alice_in_Glasses.rar/file		
https://www.mediafire.com/file/waw6u7t5nwdlnnx/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529.rar/file		
https://www.mediafire.com/file/41bx1hfe43pf24v/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210829a.rar/file		
https://www.mediafire.com/file/v1ii940w9gy56ty/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Azur_Lane_HMS_Sirius.rar/file		
https://www.mediafire.com/file/oraxft90mj8p7lr/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210831a.rar/file		
https://www.mediafire.com/file/qymjyhx1ontawuh/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210721b.rar/file		
https://www.mediafire.com/file/1ppi85me5zb0cb8/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20211001a.rar/file		
https://www.mediafire.com/file/ygrf2dzu08w2zap/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Destiny_Child_-_Rita_%2528Paradise_Exiled_ver.%2529.rar/file		
https://www.mediafire.com/file/03dc7y89oyod4ed/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210827a.rar/file		
https://www.mediafire.com/file/6hh0apid4ib7qsg/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Fancy_Me.rar/file		
https://www.mediafire.com/file/6f0z9yq73a6b8bd/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210820a.rar/file		
https://www.mediafire.com/file/0too4qjeft6f9ln/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Halloween_Nightmare.rar/file		
https://www.mediafire.com/file/81a4kjoejymj9e4/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210721c.rar/file		
https://www.mediafire.com/file/9hg0ddxu94unj8a/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210825a.rar/file		
https://www.mediafire.com/file/7a6vue3zkopxgk2/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210718a.rar/file		
https://www.mediafire.com/file/pe80zv5i05z8sc2/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210806a.rar/file		
https://www.mediafire.com/file/3jg5wfg1mp9obgu/DJAWA_Photo_-_Bambi_20210828a.rar/file		
https://www.mediafire.com/file/354gfphqlvyz1nq/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210911a.rar/file		
https://www.mediafire.com/file/ti3jday6djqvvgm/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Nightcrawler.rar/file		
https://www.mediafire.com/file/r0hjs14ad137h39/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Nuit_de_No%25C3%25ABl.rar/file		
https://www.mediafire.com/file/ikury0o832adwja/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Nurse_Nation_%2528Black_ver%2529.rar/file		
https://www.mediafire.com/file/8rzmqb1frv9ivqq/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Nurse_Nation_%2528White_ver%2529.rar/file		
https://www.mediafire.com/file/8k9totlie0u9gch/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210717a.rar/file		
https://www.mediafire.com/file/gsxwp1wb48z09pj/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210718b.rar/file		
https://www.mediafire.com/file/eyte6oviajfcl56/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210723a.rar/file		
https://www.mediafire.com/file/xft6lfl45awvr3e/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210825b.rar/file		
https://www.mediafire.com/file/qlzdsoqcx7jz9bc/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Sheer_Bunny_Maid.rar/file		
https://www.mediafire.com/file/w8v4dhjjcqz4m6n/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210820b.rar/file		
https://www.mediafire.com/file/yfsyq1bkqbuq397/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Tifa_Lockhart.rar/file		
https://www.mediafire.com/file/0bvokrj34y5qkx0/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210918a.rar/file		
https://www.mediafire.com/file/lcqwx91cd13b3sk/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210901a.rar/file		
https://www.mediafire.com/file/d218fy2n1t0cbio/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_20210809a.rar/file		
https://www.mediafire.com/file/a3ewnjl2xaqko3a/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529o.rar/file		
https://www.mediafire.com/file/ixq3vlh3fs2f4vq/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529.rar/file		
https://www.mediafire.com/file/7zfsohy0fivdfng/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_%25E2%2580%259CReine_de_Blanc_%2528B-side%2529%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/kxixdqrxrbqo56n/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_%25E2%2580%259CReine_de_Blanc%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/a1hpbh5i9pvy6ye/DJAWA_Photo_-_Bambi_%2528%25EB%25B0%25A4%25EB%25B9%2584%2529_-_Sonico-w_Micro-top_%2528Super_Sonico%2529.rar/file		
https://www.mediafire.com/file/2fuuikhfsscj7jp/DJAWA_Photo_-_Bomi_%2528%25EB%25B3%25B4%25EB%25AF%25B8%2529_%25E2%2580%259CBomistry_%25231%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/fr16l465i0vkym6/DJAWA_Photo_-_Bomi_%2528%25EB%25B3%25B4%25EB%25AF%25B8%2529_-_%25E2%2580%259CBomistry_%25232%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/ex7hxxti28x4nw4/DJAWA_Photo_-_Bomi_%2528%25EB%25B3%25B4%25EB%25AF%25B8%2529_-_%25E2%2580%259CBomistry_%25233%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/s7aln9cm88uy0h5/DJAWA_Photo_-_Echi_-_Reine_des_Lapins.rar/file		
https://www.mediafire.com/file/hckqp3vsrl9pa23/DJAWA_Photo_-_Echi_-_Staycation_%25233.rar/file		
https://www.mediafire.com/file/5s73143w4pvifhk/DJAWA_Photo_-_HaNari_%2528%25ED%2595%2598%25EB%2582%2598%25EB%25A6%25AC%2529_20210819a.rar/file		
https://www.mediafire.com/file/ue3jcc2lyfohc75/DJAWA_Photo_-_HaNari_%2528%25ED%2595%2598%25EB%2582%2598%25EB%25A6%25AC%2529_-_Red_Orange_%2526_Cool_Mint.rar/file		
https://www.mediafire.com/file/rdcchm6bq0rcjui/DJAWA_Photo_-_HaNari_%2528%25ED%2595%2598%25EB%2582%2598%25EB%25A6%25AC%2529_-_Snow_Cat_%25232.rar/file		
https://www.mediafire.com/file/2ye7tzuqcg1060r/DJAWA_Photo_-_Heihwa_%2528%25EC%2584%25A4%25EC%2597%25B0%2529_20210725a.rar/file		
https://www.mediafire.com/file/mw4e4cp5912kjqx/DJAWA_Photo_-_Heihwa_%2528%25EC%2584%25A4%25EC%2597%25B0%2529_-_Hip_Addiction_Maid.rar/file		
https://www.mediafire.com/file/jg3gjzuwuedy4ul/DJAWA_Photo_-_Hizzy_%2528%25ED%259E%2588%25EC%25A7%2580%2529_-_%25E2%2580%259CSelf_Satisfaction_VOL._2%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/s2htk0du47jc00j/DJAWA_Photo_-_Jamong_%2528%25EC%259E%2590%25EB%25AA%25BD%2529_20210806a.rar/file		
https://www.mediafire.com/file/jyi27tvxa3u17ua/DJAWA_Photo_-_Jang_Joo_%2528%25EC%259E%25A5%25EC%25A3%25BC%2529_-_Shuten_Douji_Maid.rar/file		
https://www.mediafire.com/file/2ub3sv0ssmbte97/DJAWA_Photo_-_Jeong_Jenny_20210907a.rar/file		
https://www.mediafire.com/file/c9vbvetjxx4lphx/DJAWA_Photo_-_Jeong_Jenny_20210919a.rar/file		
https://www.mediafire.com/file/bqrdqp2kau7j1pp/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Christmas_Special.rar/file		
https://www.mediafire.com/file/v3q89x32300q4f9/20220109a.7z/file		
https://www.mediafire.com/file/e2g72ywv98nlb9a/DJAWA_Photo_-_Jeong_Jenny_20210726a.rar/file		
https://www.mediafire.com/file/sq812utbb26uh6z/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Eternal_Return_RIO_%2528Black_Survival%2529.rar/file		
https://www.mediafire.com/file/pmfwu93genycqsd/DJAWA_Photo_-_Jeong_Jenny.rar/file		
https://www.mediafire.com/file/7dm3mp78sujxw5l/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_20210905a.rar/file		
https://www.mediafire.com/file/8vnhp2m84vqjbz6/DJAWA_Photo_-_Jeong_Jenny_20210906a.rar/file		
https://www.mediafire.com/file/8lddw28zvhb0qf7/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_Maid_Mansion.rar/file		
https://www.mediafire.com/file/a40klle63k2jgxu/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_NieR_Automata_2B.rar/file		
https://www.mediafire.com/file/oa3108h8vtdc1m0/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_20210831a.rar/file		
https://www.mediafire.com/file/zkbnark4rjg0mrj/DJAWA_Photo_-Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_20210725b.rar/file		
https://www.mediafire.com/file/o0bwrcubvp99vuz/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_20210725a.rar/file		
https://www.mediafire.com/file/fc3qttoc2q6cxbk/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_20210722a.rar/file		
https://www.mediafire.com/file/o2znp1p5idfz7w5/DJAWA_Photo_-_Jeong_Jenny_20210724a.rar/file		
https://www.mediafire.com/file/lqitkm7f4988r4f/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_%25E2%2580%259CGirls%2527_Frontline_-_Type_95_%2528Pure_White_Graduation_ver.%2529%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/xven65fszh462bp/DJAWA_Photo_-_Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_%25E2%2580%259CSailor_Stripes%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/tghh0scn2otg09d/DJAWA_Photo_-Jeong_Jenny_%2528%25EC%25A0%2595%25EC%25A0%259C%25EB%258B%2588%2529_-_%25E2%2580%259CThe_Lord_of_Nightmares%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/131qj24jmw8setm/DJAWA_Photo_-_Kang_In-kyung_%2528%25EA%25B0%2595%25EC%259D%25B8%25EA%25B2%25BD%2529.rar/file		
https://www.mediafire.com/file/r1iye6atqmur4kg/DJAWA_Photo_-_Kang_In-kyung_%2528%25EA%25B0%2595%25EC%259D%25B8%25EA%25B2%25BD%2529_-_%25E2%2580%259CEromanga_Sensei%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/azgsy97a0o100s9/DJAWA_Photo_-_Kang_In-kyung_%2528%25EA%25B0%2595%25EC%259D%25B8%25EA%25B2%25BD%2529_-_%25E2%2580%259CMaid_in_Lace_Limitation%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/7t732fy0m9l6eaw/DJAWA_Photo_-_Kang_In-kyung_%2528%25EA%25B0%2595%25EC%259D%25B8%25EA%25B2%25BD%2529_-_%25E2%2580%259CMasked_Pirate%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/osffau80i89awkq/DJAWA_Photo_-_Kang_In-kyung_%2528%25EA%25B0%2595%25EC%259D%25B8%25EA%25B2%25BD%2529_20210903a.rar/file		
https://www.mediafire.com/file/xez1vn9c1u2zd76/DJAWA+Photo+–+Kang+In-kyung+(강인경)+“Rescue+Me”.rar/file		
https://www.mediafire.com/file/sc6rnygmr652kfn/DJAWA_Photo_-_Kang_In-kyung_%2528%25EA%25B0%2595%25EC%259D%25B8%25EA%25B2%25BD%2529_-_%25E2%2580%259CSummoner_Girl%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/ntzxkdk7u2umpmx/DJAWA_Photo_-_Maruemon_%2528%25EB%25A7%2588%25EB%25A3%25A8%25EC%2597%2590%25EB%25AA%25BD%2529_20210721a.rar/file		
https://www.mediafire.com/file/7ciqn60pa4vaf4l/DJAWA_Photo_-_Maruemon_%2528%25EB%25A7%2588%25EB%25A3%25A8%25EC%2597%2590%25EB%25AA%25BD%2529_20210823a.rar/file		
https://www.mediafire.com/file/e5odkh0bjax709r/DJAWA_Photo_-_Maruemon_%2528%25EB%25A7%2588%25EB%25A3%25A8%25EC%2597%2590%25EB%25AA%25BD%2529_20210806a.rar/file		
https://www.mediafire.com/file/odzrm73954mmt88/DJAWA_Photo_-_Maruemon_%2528%25EB%25A7%2588%25EB%25A3%25A8%25EC%2597%2590%25EB%25AA%25BD%2529_-_%25E2%2580%259CKnotting_Class_%25233%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/pjyoljntj03g6dm/DJAWA_Photo_-_Maruemon_%2528%25EB%25A7%2588%25EB%25A3%25A8%25EC%2597%2590%25EB%25AA%25BD%2529_-_%25E2%2580%259CRealised_Feral_Cat%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/e4kg4e2hnhjlez5/DJAWA_Photo_-_Maruemon_%2528%25EB%25A7%2588%25EB%25A3%25A8%25EC%2597%2590%25EB%25AA%25BD%2529_20210823b.rar/file		
https://www.mediafire.com/file/1qfl27bi8oigcc7/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Azur_Lane_IJN_Atago_%2526_Takao.rar/file		
https://www.mediafire.com/file/v8bf6ota3hd523x/DJAWA_Photo_-_Cyberpunk_Girl_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529.rar/file		
https://www.mediafire.com/file/1mveviowpj2wkap/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Kitsune_Miko_%2528A_ver%2529.rar/file		
https://www.mediafire.com/file/j73ce9tnygcr0kc/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_March_Hare.rar/file		
https://www.mediafire.com/file/ph6t1lpeyztea4j/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529.rar/file		
https://www.mediafire.com/file/ypktj5l14eewswq/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Realise_Loveliness.rar/file		
https://www.mediafire.com/file/zyn1nv8ma6ia8zm/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Swimming_Lessons_%25238.rar/file		
https://www.mediafire.com/file/vbgrk28tf4wymvy/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_20210722a.rar/file		
https://www.mediafire.com/file/00kqegv66arsweu/DJAWA_Photo_-_Mimmi_%2528%25EB%25B0%2588%25EB%25AF%25B8%2529_-_Witch%2527s_Witchcraft.rar/file		
https://www.mediafire.com/file/hq53bqukzcctv5f/DJAWA_Photo_-_Mozzi_%2528%25EB%25AA%25A8%25EC%25B0%258C%2529_%2526_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_20211009a.rar/file		
https://www.mediafire.com/file/6jdzlzgqw2bd5ks/DJAWA_Photo_-_Parkhaag_20210826a.rar/file		
https://www.mediafire.com/file/x2vc2kesm5jnffk/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Barely_Covering_Girl.rar/file		
https://www.mediafire.com/file/22ycuv57jtc5m1l/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Black_Cat_%2526_Gold_Python.rar/file		
https://www.mediafire.com/file/db524ned5hzve49/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_20210804a.rar/file		
https://www.mediafire.com/file/rhxyba9vcq3ux9j/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Cozy_White.rar/file		
https://www.mediafire.com/file/k76gfscyd11udnp/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_20210813a.rar/file		
https://www.mediafire.com/file/96l4gip9kz8ak2j/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_20210723a.rar/file		
https://www.mediafire.com/file/9g0c2uwfonl83kv/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Leather_Black_Schoolgirl.rar/file		
https://www.mediafire.com/file/j0z7uhdgti84h2y/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Loose_and_Tight_Salmon_Pink.rar/file		
https://www.mediafire.com/file/fb7o1v3gp0p8l3u/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Private_Athletic_Class%25C2%25B2.rar/file		
https://www.mediafire.com/file/zsm52i152os2j0m/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Staycation_2.rar/file		
https://www.mediafire.com/file/zdes6d47c6oo2c7/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_-_Staycation.rar/file		
https://www.mediafire.com/file/gwpxn5alows1ymg/DJAWA_Photo_-_Pia_%2528%25ED%2594%25BC%25EC%2595%2584%2529_20210725a.rar/file		
https://www.mediafire.com/file/exjo2f3o03tejzo/DJAWA_Photo_-_Pia.rar/file		
https://www.mediafire.com/file/wch37m2vi920gdp/DJAWA_Photo_-_Pian_%2528%25ED%2594%25BC%25EC%2595%2588%25ED%2599%2594%2529_20210822a.rar/file		
https://www.mediafire.com/file/jvyzfo9fyz8ooi8/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_%255BKimetsu_no_Yaiba%255D_Mitsuri_Kanroji.rar/file		
https://www.mediafire.com/file/l48xummvjnmr2ff/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_%255BSquid_Game%255D_Triangle_Soldier.rar/file		
https://www.mediafire.com/file/hczklxupw3dgaz5/DJA+20220107a.7z/file		
https://www.mediafire.com/file/k8zw0096q9ejo9q/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Bikini_Vacation_%25231.rar/file		
https://www.mediafire.com/file/5fa07xlfucqd65b/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Cute_Pink.rar/file		
https://www.mediafire.com/file/c0tgte3jc6fq8tz/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Holidays_in_Eden.rar/file		
https://www.mediafire.com/file/48n6up2jwta3vxd/DJAWA_Photo_-_Son_Ye-Eun_20211003a.rar/file		
https://www.mediafire.com/file/kgket2jukajknlm/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_Staycation_%25234.rar/file		
https://www.mediafire.com/file/q1ht6me71pawq0q/DJAWA_Photo_-_Son_Ye-Eun_%2528%25EC%2586%2590%25EC%2598%2588%25EC%259D%2580%2529_-_%25E2%2580%259CSwimming_Lessons_%25236%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/wwsob8lfaobmpk1/DJAWA_Photo_-_Song_Hana_20210726a.rar/file		
https://www.mediafire.com/file/r7b9sl4kftqhapu/220206836a.7z/file		
https://www.mediafire.com/file/j93xsy8wsb1l0pv/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_%2526_Mozzi_%2528%25EB%25AA%25A8%25EC%25B0%258C%2529_-_%25E2%2580%259CSwimming_Lessons_%25235%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/geckg3n8p8pwzad/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_20210809a.rar/file		
https://www.mediafire.com/file/lhs7p0se5gy0hvx/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_-_Gata_Rosa.rar/file		
https://www.mediafire.com/file/3kl2p03vk4tbqfx/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_20210717a.rar/file		
https://www.mediafire.com/file/rmp8lq8608pgoze/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_-_My_Little_Bunny.rar/file		
https://www.mediafire.com/file/tjkahgxkgi8jaep/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_-_Sheer_Qipao_Girl.rar/file		
https://www.mediafire.com/file/9ekylr5oo03tr25/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_20210804a.rar/file		
https://www.mediafire.com/file/sb5fqrennuqaiq7/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_-_%25E2%2580%259CKnotting_Class%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/ampor3yymsvay6h/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529_-_%25E2%2580%259CNeed_Your_Approval%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/eauikwle87rrhfu/DJAWA_Photo_-_Sonson_%2528%25EC%2586%2590%25EC%2586%2590%2529.rar/file		
https://www.mediafire.com/file/1kygr3kvd2qvcey/DJAWA_Photo_-_Tae_Ri_%2528%25ED%2583%259C%25EB%25A6%25AC%2529_%2526_Bomi_%2528%25EB%25B3%25B4%25EB%25AF%25B8%2529_-_%25E2%2580%259CDevil_666_%2526_Angel_777%25E2%2580%259D.rar/file		
https://www.mediafire.com/file/cmntgd5y4lg5cr1/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_%255BLoL%255D_Ahri_The_Baddest.rar/file		
https://www.mediafire.com/file/ez2dvmleu4npkp5/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_Azur_Lane_IJN_Yamashiiro.rar/file		
https://www.mediafire.com/file/ftm4uffgwrwrwse/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_Christmas_Special_2020.rar/file		
https://www.mediafire.com/file/msnkxsm70tk7a1d/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_Overheated_K2_%2528Girls_Frontline%2529.rar/file		
https://www.mediafire.com/file/w7wkwc0lrzdn1pc/DJZia_-_P_H_G.7z/file		
https://www.mediafire.com/file/juo1nyxaf3wxnyf/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_Perrault_The_Milk_Thief_%2528Last_Origin%2529.rar/file		
https://www.mediafire.com/file/kpdf53ngj4y9a2c/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_20210725a.rar/file		
https://www.mediafire.com/file/85b2rcanovzk4ob/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_Swimming_Lessons.rar/file		
https://www.mediafire.com/file/ye2z8za98vo7kwg/DJAWA_Photo_-_Zia_%2528%25EC%25A7%2580%25EC%2595%2584%2529_-_The_Kunoichi.rar/file		
https://www.mediafire.com/file/z4mkjfqbjlp8nh3/DJAWA_Photo_-_Zzyuri_%2528%25EC%25AE%25B8%25EB%25A6%25AC%2529_-_Alluring_White.rar/file		
https://www.mediafire.com/file/y4wtvlf4vb7q9ye/DJAWA_Photo_%25E2%2580%2593_Parkhaag_%2528%25EB%25B0%2595%25ED%2595%2598%25EC%2595%2585%2529_-_Swimming_Lessons_%25239.rar/file	
'''

for url in urls.split():
  mediafire_dl.download(url, output = None, quiet = False)