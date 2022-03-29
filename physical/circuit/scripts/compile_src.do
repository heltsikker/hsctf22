quietly set source_path ".."
quietly set target_path "$source_path/sim"
set lib_name "work"

quietly vlib $target_path/$lib_name
quietly vmap $lib_name $target_path/$lib_name

vcom -2008 -work $lib_name $source_path/pin.vhd
vcom -2008 -work $lib_name $source_path/circuit.vhd
