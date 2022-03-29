from gmpy2 import isqrt
import time

def FermatAttack(n):
	a = b = isqrt(n)
	b2 = pow(a,2)-n
	while pow(b,2)!=b2:
		a += 1
		b2 = pow(a,2)-n
		b = isqrt(b2)
	return a+b, a-b

# Ciphertext
c = [18963281541601545202026193774036739243848493762797378160999973433168400243715687073212148627780725678831736402228445217810204713289075166241746056933484391803103639586271908579121487909376641504717133742187761792269785510425466197613830822682089117042087444445766465575758970702005631943750333460050639887390172737275349811003889483965796128040463222027887616249021459156105226203243124568655787815480315717585564910138755390407349722273701872216323868599735900971594287509160855381387475363622644809869494762454442200241682627309744027105015804553441359646201476593852920230230296298862726609504426197893357149034005, 3493836687847385908960873021357138366029159924117697398098126254549598249749116527038855436887596601153452922601267310936698884616025266469233330305842111243313751150313554035172890141895877495703707897944857296856481421809869172717876638675165485580852805186681556694115424404568376059352207383967970186712824905640859286884900950957665066830325069971897180362148280927261372704731683451455933981042059276617746458278985395397203423364920195361005628046669463193722925381934953614781286200298472109576828188765014347148894120339433968828521479209574498046234230004485017259840706806905382372441283680313978162364127, 17239727321143079236268552517114936277649479819118610637151326725537148728765529572497328046056645655337401282807563513247544207410297252956639783189924315506813214735419315587308403964684275195742416746944999539321030969412589970102079940705938695809736221770748992464761155921224755178890068769963219502425964531269155694643879924128591487005371793744568600187572299280187733253746811426818853043058031767277012088955008181726273562697946575114305746150296785136528127582300212246342089870676154377780873925296317701316762519628433596099063859695632299640925222003131577378522338368855471150449920721804851872533223, 8534287517252017175533858765536197914524554165858430174375360843164614897498593569284613227526205174147860484907588481980286655613012929106718769395767098167419566953781755888570388561681339807641471353155906031500611745615401014339641907110532977543169325370055576020983999019376326592029858981406790083084540525349875176643488118889667719322516552828359379338627596658243251209181396064228759338766789100768983902083774713252612862019945093465473321802183195074381238669420263945828775732387821755227474214224447148699910610018404590653741166648364079393549397994747335741896621329258456837913003669284634060822423, 9375826876937716946894632799657496726828023409470678145366038202615712315136218734018065949745113437549825808162863595548862476571797557955844020109949668443832607131939571526269548039917069403784936019233957347709530703809185713747419879726047973467055998135045872065512033705945459050651641945042313428908410183356227439645647471505166624356738901724238972803221923828105558002766716844376628761773116574217365233800826602234699915358311926899469077538664977908274953410830144397986718088278422899053423865540484596947315968261310545529655321756516421855475070945571365156316368261289973954892308159578261066152655, 29935835443257189270556452986879710681387347243411464334080736037912389007363589594368189228238915177413789240391476761154095630631111781094550008491619424813349592249144619647283688600393972470802277392198601214960072945050848429658882674916176316025435965287982579470859400635694675792905768670622890313729983157040376019081315841497199298687177468096235054268541815925578720532797091555969581209871390133005928603040738776470527314098279569026950267033655345590092547916794776387204144987150646979090749990901236213410298570131719350718675180219992530161892765983606647174560100000848499254030539453408656539775908, 8927081592940092233155355740990083146934497553740649766090969305852587150008639548538169007568849234410540401590780007200229249361577121888386153212345235096985086537018038971517718909256574672621910224883485525628535697371806612523102054592183726051424559877723360842096860083582805797854807094005115582935759315644031746571827302940823167627140144912491434837673828444207054918681363824280125278129574599509459858247634501551442953661520901827016538923844916525134008739836986574357871527867723779668833815924422218062738345045441019584832633442335165210921203549220723556755330816639859901139996606454509873765275, 14094553985859032760568361764575192916818816605159560288079288993806971385915889638194862834261045484594902186221223974418166217898086021032094033403034165275603205176048514350931560547178228040949177717389549863018374747426182042351142792317798236257475596324426844080140657399968700694841808540429051878464040875305289572525255672311315029212354289107521845096934214647920236268244390899013147076326399890243607144088129453689259869167616183789320079387133773732674226415785836488559224045323783390540543046770828232317516025304842154947667754707162019166890059808228040089412310017586068896723451055314776414501266, 26385364164388388935812064423033615305738661713939792773556086936785610263421489998890810363042726903691589367107774055471437174905816095104259466022600349902285985930411605594268825540695165486188018465978534066014092307630398682184520625249300713243346744025267189516196695524680254076604013042137853581728854024312178557523380015600406709799170934835297863895293786676800414174870994791130430703994171701233258723996330714251521907279754246559353093610656994751837159543607135073878394354641231574391147579112972666747300189480944689601868358460305338087234575181248064095992835497639771175266320253257310469498337, 8927081592940092233155355740990083146934497553740649766090969305852587150008639548538169007568849234410540401590780007200229249361577121888386153212345235096985086537018038971517718909256574672621910224883485525628535697371806612523102054592183726051424559877723360842096860083582805797854807094005115582935759315644031746571827302940823167627140144912491434837673828444207054918681363824280125278129574599509459858247634501551442953661520901827016538923844916525134008739836986574357871527867723779668833815924422218062738345045441019584832633442335165210921203549220723556755330816639859901139996606454509873765275, 17781596458175651689073824486568214784997288722738802122845724342349328406642379764480465051070486023983045685494136231268250497545074636385005551409654929007782169295152161624356465666189004885787109075608402224514002190735872795279158992692410192230480285709549251194181887211042309658080338437227323962802419691243624981638324468391739248354457993104504062266058055324749362453779902172128821112632938364940897852315311228964289924287985723253628354808899828668230066467141010556000261010692618190068673027653225318342590403804721664352685515468486726257418819322939889158589520830203349121931215375581064434162551, 21834989804792459964315185800149534963597211655448110971025225486155142090242150793251986120535268274590922195310005510714565106095821070892071983585566938997356760919900970117396062925281342134893613351353259515287714862235455667083428179820911507454937387815450632312875622762421869336561235907548391275537864756518916386424689503420124439707057538041268149610164073838918410303081152565593039081747079572538026267165425364378778614153730031652278894839285963763267330114393719615000352235265007973480289934841143887885978003896953105382294976454531267768864266313928587025352597990220581068483465905201843695382047, 27369594290097617855641374849344966924127913273055457733373333545067162563431089618401345158346493382589654974585137408181946199011902266516014592453710925698854767991065248070439489922184966191823966191442966418320055485826751784504074908215543088404244203319312151937222034469789659399569973819932471266079571187607015351874586045755856106387197208180435755163343751737999018685742838126775009680543016223333029582103638910367511583151665867188587534560026253623340729492400887285413173969153516446287992327092608504232890476295858066455841257460277329663700508952083193854201027522091996947120164823252114759224537, 2906529167776477183826378878808505684794018089858879416579806994400244616853506757956404758992473006658798400962309135837151533417369073852169105457861177671291164429642182728907083203290319008686044489741756076796333221453953599744570129844507202142032408682162029167308456489443821800718957595158351853745511898453205271377073593074877253704732134297641664500253104217809032189899182994794244251686687156423012292005992923313529148468468362628939816587564947550005522575328849465114311517289302703407597451021152521137588983109867556654771844127266110887945745200505861814001347611393328794625143610396707671391166, 9090974392561541285929366350993325937313901522881874461383064261337782869737217814578669728707477107769572644703251642123483169454125551686344242852716306600048691056386497660140615742869360309410035147182488601641052660675308345740622332434954342997148687773571053982669497554795049323450780212049162785942091310392844054007440292474623972955894622118229429555368059288725144575558901820132946035960853768992531039907546568443081611499005320494771484551080544838899122208764419653726505711508542527901170136648073759086280655784659715116858959708577203234171196784666550663619319048539935412080808886729003945491290, 27369594290097617855641374849344966924127913273055457733373333545067162563431089618401345158346493382589654974585137408181946199011902266516014592453710925698854767991065248070439489922184966191823966191442966418320055485826751784504074908215543088404244203319312151937222034469789659399569973819932471266079571187607015351874586045755856106387197208180435755163343751737999018685742838126775009680543016223333029582103638910367511583151665867188587534560026253623340729492400887285413173969153516446287992327092608504232890476295858066455841257460277329663700508952083193854201027522091996947120164823252114759224537, 4398320746498505967951253520132318623668364405452565177539239794517465160390933280467934208561089699052683817802292136006399513585881136874731635846052136637947031437871326573655619307716645353033918621858562452379256188860347357384940559173024304599705879521552706916012678906148945765688250275072458997137494701376106282045270271533355403560571263818114915743617765523924865199570763659812541126429305362993846504664341401966297545505058229991797433765168396522712914129687181625592717493620654620889596196094086065571704505074365664293421660587688751476533190282409875894792511204889166837798783524602031765101309, 21094856039711452542470274013849078595610510482948591612266603511469402229244075623296691262097737779165264414628209283084673220628402415193114094650013090141838315451979991889034362767878604713175726004514906162171705422011859610570694064907622709163461706137746977553066330812940862761578599171714051746422465765713644933542889104081473796763056734814191685799538601093161453187441661363630101288165874155465771261659294132996004331839112264744417249911194179890208544432364603785083525902243551769990320656060650596369578286165030765101011197337383567308411897391437350312165320604385545642959416367142055076291632, 26971563686839847291747065447561324694272129960942747962784350469575937380536361723977640667266061957269367850686163524883515979502645039452223530587206472556269812201567515272584692902865182208471846649166084019020973738607745718391663039541289009383730094315301145676520269968043323813261886335944990175027834281549585696445715472586168243853092914547874759047587128060474057186899245086903060077657655301786813088464256059110596293050802020682513303504268500738156584729691830056292417915480174087877920261896100251237541995686090018541827996129295569478192563045745220327682667970664751283452884447081775228294557, 14747258582714835393071906755443276832628781653191222513073686859257674177370702358798254026785312027415893587367229282600883017401519392045746749538327486783797786546754112667030244595159911453202339495227305885361843303774933138715594457971879429537344034953362804196496258071234679270391315147825881143910930317705470214013642292470758638183506604581041851027118972368670215108904691756549763423413115380564348867528417669989333441911258730588300515313156011419776931573888003659831645112391510265188734997738623391276999478598020846675421019703000878797478635411507915252845734733801834481849251845130653768103498, 26385364164388388935812064423033615305738661713939792773556086936785610263421489998890810363042726903691589367107774055471437174905816095104259466022600349902285985930411605594268825540695165486188018465978534066014092307630398682184520625249300713243346744025267189516196695524680254076604013042137853581728854024312178557523380015600406709799170934835297863895293786676800414174870994791130430703994171701233258723996330714251521907279754246559353093610656994751837159543607135073878394354641231574391147579112972666747300189480944689601868358460305338087234575181248064095992835497639771175266320253257310469498337, 9090974392561541285929366350993325937313901522881874461383064261337782869737217814578669728707477107769572644703251642123483169454125551686344242852716306600048691056386497660140615742869360309410035147182488601641052660675308345740622332434954342997148687773571053982669497554795049323450780212049162785942091310392844054007440292474623972955894622118229429555368059288725144575558901820132946035960853768992531039907546568443081611499005320494771484551080544838899122208764419653726505711508542527901170136648073759086280655784659715116858959708577203234171196784666550663619319048539935412080808886729003945491290, 8927081592940092233155355740990083146934497553740649766090969305852587150008639548538169007568849234410540401590780007200229249361577121888386153212345235096985086537018038971517718909256574672621910224883485525628535697371806612523102054592183726051424559877723360842096860083582805797854807094005115582935759315644031746571827302940823167627140144912491434837673828444207054918681363824280125278129574599509459858247634501551442953661520901827016538923844916525134008739836986574357871527867723779668833815924422218062738345045441019584832633442335165210921203549220723556755330816639859901139996606454509873765275, 4398320746498505967951253520132318623668364405452565177539239794517465160390933280467934208561089699052683817802292136006399513585881136874731635846052136637947031437871326573655619307716645353033918621858562452379256188860347357384940559173024304599705879521552706916012678906148945765688250275072458997137494701376106282045270271533355403560571263818114915743617765523924865199570763659812541126429305362993846504664341401966297545505058229991797433765168396522712914129687181625592717493620654620889596196094086065571704505074365664293421660587688751476533190282409875894792511204889166837798783524602031765101309, 4398320746498505967951253520132318623668364405452565177539239794517465160390933280467934208561089699052683817802292136006399513585881136874731635846052136637947031437871326573655619307716645353033918621858562452379256188860347357384940559173024304599705879521552706916012678906148945765688250275072458997137494701376106282045270271533355403560571263818114915743617765523924865199570763659812541126429305362993846504664341401966297545505058229991797433765168396522712914129687181625592717493620654620889596196094086065571704505074365664293421660587688751476533190282409875894792511204889166837798783524602031765101309, 9090974392561541285929366350993325937313901522881874461383064261337782869737217814578669728707477107769572644703251642123483169454125551686344242852716306600048691056386497660140615742869360309410035147182488601641052660675308345740622332434954342997148687773571053982669497554795049323450780212049162785942091310392844054007440292474623972955894622118229429555368059288725144575558901820132946035960853768992531039907546568443081611499005320494771484551080544838899122208764419653726505711508542527901170136648073759086280655784659715116858959708577203234171196784666550663619319048539935412080808886729003945491290, 17781596458175651689073824486568214784997288722738802122845724342349328406642379764480465051070486023983045685494136231268250497545074636385005551409654929007782169295152161624356465666189004885787109075608402224514002190735872795279158992692410192230480285709549251194181887211042309658080338437227323962802419691243624981638324468391739248354457993104504062266058055324749362453779902172128821112632938364940897852315311228964289924287985723253628354808899828668230066467141010556000261010692618190068673027653225318342590403804721664352685515468486726257418819322939889158589520830203349121931215375581064434162551, 21834989804792459964315185800149534963597211655448110971025225486155142090242150793251986120535268274590922195310005510714565106095821070892071983585566938997356760919900970117396062925281342134893613351353259515287714862235455667083428179820911507454937387815450632312875622762421869336561235907548391275537864756518916386424689503420124439707057538041268149610164073838918410303081152565593039081747079572538026267165425364378778614153730031652278894839285963763267330114393719615000352235265007973480289934841143887885978003896953105382294976454531267768864266313928587025352597990220581068483465905201843695382047, 30217504872552610339597916582034767592357794384417228934462810955556418804697372415599991101752932255771493313846295671307043040547691028837512445177000446512695497766398697669626732210920865602638720794170008499787464762118364687257558857791363724491898020917867401518643571110919320975066503559415196788753462174432236968224337399043046126814804431220971325244622354803045640827446546071549489124399990307376763725942078706257836821342721961040979859377108032016696824015452172145280511346040354596403188630687668264367761800413595512073026848674876723680159271591384781486566695442465245916900855218252029103931884]
N = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123918320946935231356245322611350669435062332237426977018743784893420014488530923324428250820994863161368653379766183041813622447954779005323408047238533046412963394545462966539444902926639207361454524114379705685443395684658192563915963012257512925967853039018359190511427650533913311361175234306512212671679120144689089
e = 65537

# Attack
print("Running Fermat attack on RSA.")
start_time = time.time()
p, q = FermatAttack(N)
end_time = time.time()
print(f"Attack successful: {N==p*q}.")
print(f"Attack execution time: {end_time-start_time:.3f} seconds.")

# RSA
start_time = time.time()
phi_n = (p-1)*(q-1)
d = pow(e, -1, phi_n)
priv_key = [p,q,d]
pub_key = [N,e]
decrypted_m = [int(pow(i,d,N)) for i in c]
recovered_msg = ''.join([chr(i) for i in decrypted_m])
end_time = time.time()

print(f"\nPrivate key:\np = {p}\nq = {q}\nd = {d}")
print(f"Public key:\nN = {N}\ne = {e}")
print(f"Encoded decrypted message: {decrypted_m}.")
print(f"Recovered message: {recovered_msg}.")
print(f"RSA execution time: {end_time-start_time:.3f} seconds.")

